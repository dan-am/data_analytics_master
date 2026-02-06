# Phase 8: Deployment

## Überblick
Diese Phase konzentriert sich auf die Vorbereitung des Patientensegmentierungsmodells für den Produktionseinsatz.

## Ziele
- Deployment-Strategie dokumentieren
- Inferenz-Pipeline erstellen
- API entwickeln (falls erforderlich)
- Monitoring und Wartung planen
- Benutzerdokumentation erstellen

## Deployment-Strategie

### 1. Deployment-Optionen

#### Option A: Batch-Vorhersagen
- Modell in geplanten Intervallen ausführen
- Patientendaten in Stapeln verarbeiten
- Segmentierung periodisch aktualisieren

#### Option B: Echtzeit-API
- REST-API für Vorhersagen auf Abruf
- Integration mit Gesundheitssystemen
- Vorhersagen mit geringer Latenz

#### Option C: In Anwendung eingebettet
- Modell mit Anwendung verpacken
- Lokale Vorhersagen
- Keine externen API-Aufrufe erforderlich

### 2. Deployment-Checkliste

- [ ] Modellartefakte gespeichert und versioniert
- [ ] Vorverarbeitungs-Pipeline dokumentiert
- [ ] Abhängigkeiten dokumentiert (requirements.txt)
- [ ] Inferenz-Skript getestet
- [ ] API-Endpunkte entworfen (falls zutreffend)
- [ ] Leistungsbenchmarks erstellt
- [ ] Monitoring-Plan definiert
- [ ] Rollback-Strategie vorbereitet

## Beispiel Inferenz-Skript

```python
"""
Inferenz-Skript zur Patientensegmentierung
"""

import joblib
import pandas as pd
import numpy as np
from pathlib import Path

class PatientenSegmentierungPredictor:
    """Klasse zur Durchführung von Patientensegmentierungs-Vorhersagen."""
    
    def __init__(self, modell_pfad, scaler_pfad=None):
        """
        Predictor initialisieren.
        
        Args:
            modell_pfad: Pfad zum gespeicherten Modell
            scaler_pfad: Pfad zum gespeicherten Scaler (optional)
        """
        self.modell = joblib.load(modell_pfad)
        self.scaler = joblib.load(scaler_pfad) if scaler_pfad else None
        
    def vorverarbeiten(self, daten):
        """Eingabedaten vorverarbeiten."""
        if self.scaler:
            daten_skaliert = self.scaler.transform(daten)
            return daten_skaliert
        return daten
    
    def vorhersagen(self, daten):
        """
        Patientensegmente vorhersagen.
        
        Args:
            daten: DataFrame mit Patienten-Features
            
        Returns:
            Array mit Segmentvorhersagen
        """
        daten_verarbeitet = self.vorverarbeiten(daten)
        vorhersagen = self.modell.predict(daten_verarbeitet)
        return vorhersagen
    
    def vorhersagen_mit_konfidenz(self, daten):
        """
        Vorhersagen mit Konfidenzwerten (falls vom Modell unterstützt).
        
        Returns:
            vorhersagen, konfidenz_werte
        """
        daten_verarbeitet = self.vorverarbeiten(daten)
        vorhersagen = self.modell.predict(daten_verarbeitet)
        
        if hasattr(self.modell, 'predict_proba'):
            konfidenz = np.max(self.modell.predict_proba(daten_verarbeitet), axis=1)
            return vorhersagen, konfidenz
        
        return vorhersagen, None
    
    def segment_profil_abrufen(self, segment_id):
        """Eigenschaften eines bestimmten Segments zurückgeben."""
        segment_profile = {
            0: "Hochrisiko-Patienten mit intensivem Betreuungsbedarf",
            1: "Patienten mit mittlerem Risiko und chronischen Erkrankungen",
            2: "Patienten mit niedrigem Risiko und Präventionsbedarf",
            3: "Gesunde Patienten für Routineuntersuchungen"
        }
        return segment_profile.get(segment_id, "Unbekanntes Segment")


def main():
    """Beispielverwendung."""
    # Predictor initialisieren
    predictor = PatientenSegmentierungPredictor(
        modell_pfad='../models/patient_segmentation_model.pkl',
        scaler_pfad='../models/scaler.pkl'
    )
    
    # Neue Patientendaten laden
    neue_patienten = pd.read_csv('neue_patienten.csv')
    
    # Vorhersagen durchführen
    segmente = predictor.vorhersagen(neue_patienten)
    
    # Zum DataFrame hinzufügen
    neue_patienten['segment'] = segmente
    
    # Segmentbeschreibungen abrufen
    neue_patienten['segment_beschreibung'] = neue_patienten['segment'].apply(
        predictor.segment_profil_abrufen
    )
    
    # Ergebnisse speichern
    neue_patienten.to_csv('patienten_segmente_ausgabe.csv', index=False)
    print(f"{len(neue_patienten)} Patienten segmentiert")


if __name__ == '__main__':
    main()
```

## REST-API-Beispiel (Flask)

```python
"""
Flask-API zur Patientensegmentierung
"""

from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Modell beim Start laden
modell = joblib.load('models/patient_segmentation_model.pkl')
scaler = joblib.load('models/scaler.pkl')

@app.route('/health', methods=['GET'])
def health_check():
    """Gesundheitscheck-Endpunkt."""
    return jsonify({'status': 'gesund', 'modell': 'geladen'})

@app.route('/predict', methods=['POST'])
def vorhersagen():
    """
    Patientensegment vorhersagen.
    
    Erwartetes JSON-Format:
    {
        "patienten": [
            {"alter": 45, "feature1": wert1, ...},
            {"alter": 60, "feature2": wert2, ...}
        ]
    }
    """
    try:
        daten = request.get_json()
        patienten_df = pd.DataFrame(daten['patienten'])
        
        # Vorverarbeiten
        patienten_skaliert = scaler.transform(patienten_df)
        
        # Vorhersagen
        segmente = modell.predict(patienten_skaliert)
        
        # Antwort formatieren
        ergebnisse = []
        for i, segment in enumerate(segmente):
            ergebnisse.append({
                'patienten_id': i,
                'segment': int(segment),
                'segment_name': f'Segment_{segment}'
            })
        
        return jsonify({'vorhersagen': ergebnisse})
    
    except Exception as e:
        return jsonify({'fehler': str(e)}), 400

@app.route('/segments', methods=['GET'])
def segmente_abrufen():
    """Informationen über verfügbare Segmente zurückgeben."""
    segmente_info = {
        '0': 'Hochrisiko-Patienten',
        '1': 'Patienten mit mittlerem Risiko',
        '2': 'Patienten mit niedrigem Risiko',
        '3': 'Gesunde Patienten'
    }
    return jsonify(segmente_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## Monitoring-Plan

### Wichtige Metriken

1. **Modellleistung:**
   - Vorhersagegenauigkeit (falls Ground Truth verfügbar)
   - Segmentverteilung über Zeit
   - Modell-Konfidenzwerte

2. **Systemleistung:**
   - Antwortzeit / Latenz
   - Durchsatz (Vorhersagen pro Sekunde)
   - Fehlerraten
   - Ressourcenverbrauch (CPU, Speicher)

3. **Datenqualität:**
   - Verteilung der Eingabedaten
   - Rate fehlender Werte
   - Werte außerhalb des Bereichs
   - Data-Drift-Erkennung

## Wartungsplan

### Regelmäßige Aufgaben

1. **Wöchentlich:**
   - Vorhersage-Logs überprüfen
   - Fehlerraten prüfen
   - Segmentverteilungen überwachen

2. **Monatlich:**
   - Modellleistung evaluieren
   - Auf Data-Drift prüfen
   - Segmentprofile überprüfen

3. **Vierteljährlich:**
   - Modell mit neuen Daten nachtrainieren
   - Segmentdefinitionen bei Bedarf aktualisieren
   - Leistungsbenchmarks durchführen

### Auslöser für Modell-Nachtraining

- Signifikanter Data-Drift erkannt
- Leistungsverschlechterung
- Neue Datenmuster aufgetreten
- Geschäftsanforderungen geändert

## Sicherheits- und Datenschutzaspekte

- **Datenschutz:** HIPAA/DSGVO-Konformität sicherstellen
- **Zugriffskontrolle:** Authentifizierung und Autorisierung implementieren
- **Datenverschlüsselung:** Daten bei Übertragung und Speicherung verschlüsseln
- **Audit-Logging:** Alle Vorhersagen und Zugriffe protokollieren
- **Modellsicherheit:** Modell vor Adversarial Attacks schützen

## Ergebnisse

- [ ] Deployment-Leitfaden (dieses Dokument)
- [ ] Inferenz-Skript
- [ ] API-Implementierung (falls zutreffend)
- [ ] API-Dokumentation
- [ ] Monitoring-Implementierung
- [ ] Benutzerhandbuch
- [ ] Wartungsplan

## Erfolgskriterien

- [ ] Modell erfolgreich bereitgestellt
- [ ] Vorhersagen sind genau und zeitnah
- [ ] Monitoring ist eingerichtet
- [ ] Dokumentation ist vollständig
- [ ] Benutzer sind geschult
- [ ] Wartungsplan ist aktiv
