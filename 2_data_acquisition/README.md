# Phase 2: Datenanschaffung

## Überblick
Diese Phase konzentriert sich auf das Sammeln und Organisieren des Patientensegmentierungs-Datensatzes.

## Ziele
- Datensatz von Kaggle herunterladen
- Datenquelle dokumentieren
- Rohdaten organisieren
- Erste Datenbewertung durchführen

## Datensatz-Informationen

**Quelle:** [Patient Segmentation Data](https://www.kaggle.com/datasets/nudratabbas/patient-segmentation-data)

**Anbieter:** Kaggle

**Autor:** Nudrat Abbas

## Verzeichnisstruktur

```
2_data_acquisition/
├── raw_data/              # Originale, unveränderte Datendateien
├── processed_data/        # Bereinigte und verarbeitete Daten
├── data_sources/          # Datenquellen-Dokumentation
└── download_data.py       # Daten-Download-Skript
```

## Anleitung

### Schritt 1: Kaggle-API einrichten

1. Kaggle-Konto erstellen unter https://www.kaggle.com
2. Kontoeinstellungen aufrufen: https://www.kaggle.com/account
3. Zum Abschnitt „API" scrollen
4. „Create New API Token" klicken
5. Die heruntergeladene `kaggle.json`-Datei in `~/.kaggle/` ablegen:

```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### Schritt 2: Abhängigkeiten installieren

```bash
pip install kaggle
```

### Schritt 3: Datensatz herunterladen

Download-Skript ausführen:

```bash
python download_data.py
```

Das Skript wird:
- Kaggle-Zugangsdaten überprüfen
- Notwendige Verzeichnisse erstellen
- Den Datensatz herunterladen
- Dokumentation erstellen

### Schritt 4: Download überprüfen

Nach dem Download das Verzeichnis `raw_data/` prüfen:

```bash
ls -lh raw_data/
```

### Schritt 5: Erste Datenexploration

Schnelle Vorschau der Daten:

```python
import pandas as pd

# Daten laden
df = pd.read_csv('raw_data/[dateiname].csv')

# Basisinformationen anzeigen
print(df.info())
print(df.head())
print(df.describe())
```

## Datenqualitäts-Checkliste

- [ ] Datensatz erfolgreich heruntergeladen
- [ ] Alle erwarteten Dateien vorhanden
- [ ] Dateigrößen sind plausibel
- [ ] Daten können fehlerfrei geladen werden
- [ ] Datenquelle dokumentiert
- [ ] Erste Zeilen-/Spaltenanzahl erfasst

## Nächste Schritte

Nach Abschluss der Datenanschaffung:
1. Datenstruktur und -inhalt überprüfen
2. Erste Beobachtungen dokumentieren
3. Weiter zu Phase 3: Datenvorbereitung

## Fehlerbehebung

**Problem:** Kaggle-Zugangsdaten nicht gefunden
- **Lösung:** Überprüfen, ob `~/.kaggle/kaggle.json` existiert und die richtigen Berechtigungen hat

**Problem:** Datensatz nicht gefunden
- **Lösung:** Datensatznamen überprüfen und sicherstellen, dass er noch auf Kaggle verfügbar ist

**Problem:** Download schlägt fehl
- **Lösung:** Internetverbindung und Kaggle-API-Status prüfen

## Referenzen

- [Kaggle-API-Dokumentation](https://github.com/Kaggle/kaggle-api)
- [Datensatz-Seite](https://www.kaggle.com/datasets/nudratabbas/patient-segmentation-data)
