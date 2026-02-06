"""
Daten-Download-Skript für das Patientensegmentierungsprojekt
Phase 2: Datenanschaffung

Dieses Skript lädt den Patientensegmentierungs-Datensatz von Kaggle herunter.

Voraussetzungen:
1. Kaggle-Konto erstellt
2. Kaggle-API-Zugangsdaten konfiguriert (~/.kaggle/kaggle.json)
3. kaggle-Paket installiert (pip install kaggle)

Verwendung:
    python download_data.py
"""

import os
import sys
from pathlib import Path
import logging

# Logging einrichten
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def verzeichnisse_einrichten():
    """Notwendige Verzeichnisse für die Datenspeicherung erstellen."""
    aktuelles_verz = Path(__file__).parent
    rohdaten_verz = aktuelles_verz / 'raw_data'
    verarbeitete_daten_verz = aktuelles_verz / 'processed_data'
    
    rohdaten_verz.mkdir(exist_ok=True)
    verarbeitete_daten_verz.mkdir(exist_ok=True)
    
    logger.info(f"Datenverzeichnisse erstellt/überprüft:")
    logger.info(f"  - Rohdaten: {rohdaten_verz}")
    logger.info(f"  - Verarbeitete Daten: {verarbeitete_daten_verz}")
    
    return rohdaten_verz, verarbeitete_daten_verz


def kaggle_zugangsdaten_pruefen():
    """Überprüft, ob die Kaggle-Zugangsdaten konfiguriert sind."""
    kaggle_json = Path.home() / '.kaggle' / 'kaggle.json'
    
    if not kaggle_json.exists():
        logger.error("Kaggle-Zugangsdaten nicht gefunden!")
        logger.error("Bitte folgende Schritte ausführen:")
        logger.error("1. https://www.kaggle.com/account aufrufen")
        logger.error("2. 'Create New API Token' klicken")
        logger.error("3. kaggle.json in ~/.kaggle/ ablegen")
        logger.error("4. Ausführen: chmod 600 ~/.kaggle/kaggle.json")
        return False
    
    logger.info("Kaggle-Zugangsdaten gefunden ✓")
    return True


def datensatz_herunterladen(rohdaten_verz):
    """Patientensegmentierungs-Datensatz von Kaggle herunterladen."""
    try:
        import kaggle
        
        datensatz_name = 'nudratabbas/patient-segmentation-data'
        logger.info(f"Lade Datensatz herunter: {datensatz_name}")
        logger.info("Dies kann einige Minuten dauern...")
        
        # Datensatz in das Rohdaten-Verzeichnis herunterladen
        kaggle.api.dataset_download_files(
            datensatz_name,
            path=str(rohdaten_verz),
            unzip=True
        )
        
        logger.info("Datensatz erfolgreich heruntergeladen! ✓")
        
        # Heruntergeladene Dateien auflisten
        dateien = list(rohdaten_verz.glob('*'))
        logger.info(f"\nHeruntergeladene Dateien ({len(dateien)}):")
        for datei in dateien:
            if datei.is_file():
                groesse_mb = datei.stat().st_size / (1024 * 1024)
                logger.info(f"  - {datei.name} ({groesse_mb:.2f} MB)")
        
        return True
        
    except ImportError:
        logger.error("kaggle-Paket nicht installiert!")
        logger.error("Installieren mit: pip install kaggle")
        return False
    except Exception as e:
        logger.error(f"Fehler beim Herunterladen des Datensatzes: {str(e)}")
        return False


def datenquellen_dokumentation_erstellen(datensatz_name='nudratabbas/patient-segmentation-data'):
    """Dokumentation über die Datenquelle erstellen."""
    aktuelles_verz = Path(__file__).parent
    dok_verz = aktuelles_verz / 'data_sources'
    dok_verz.mkdir(exist_ok=True)
    
    dok_datei = dok_verz / 'dataset_info.md'
    
    inhalt = f"""# Patientensegmentierungs-Datensatz

## Quelleninformationen

**Datensatzname:** Patient Segmentation Data

**Quelle:** Kaggle

**URL:** https://www.kaggle.com/datasets/{datensatz_name}

**Autor:** Nudrat Abbas

**Lizenz:** Lizenzinformationen auf der Kaggle-Datensatzseite prüfen

## Beschreibung

Dieser Datensatz enthält Patienteninformationen für Segmentierungsanalysen. Er ist für Healthcare-Analytics und Patienten-Clustering-Anwendungen konzipiert.

## Datensatz-Eigenschaften

- **Typ:** Multivariat
- **Fachgebiet:** Gesundheitswesen
- **Format:** CSV
- **Anwendungsfall:** Patientensegmentierung, Clustering-Analyse

## Wichtige Hinweise

1. Dies ist ein öffentlicher Datensatz von Kaggle
2. Aktuelle Beschreibung und Lizenz auf der Datensatzseite prüfen
3. Datenschutzaspekte vor Produktionseinsatz berücksichtigen
4. Datensatz in Veröffentlichungen korrekt zitieren

## Zitation

Bei Verwendung dieses Datensatzes bitte zitieren:
- Ersteller: Nudrat Abbas
- Quelle: Kaggle
- URL: https://www.kaggle.com/datasets/{datensatz_name}

## Nächste Schritte

Nach dem Download:
1. Datendateien im `raw_data/`-Verzeichnis überprüfen
2. Datenwörterbuch mit allen Feldern erstellen
3. Erste Datenqualitätsbewertung durchführen
4. Weiter zu Phase 3: Datenvorbereitung
"""
    
    with open(dok_datei, 'w') as f:
        f.write(inhalt)
    
    logger.info(f"Datenquellen-Dokumentation erstellt: {dok_datei}")


def main():
    """Hauptfunktion zur Orchestrierung des Daten-Downloads."""
    logger.info("="*60)
    logger.info("Patientensegmentierungsprojekt – Daten-Download")
    logger.info("Phase 2: Datenanschaffung")
    logger.info("="*60)
    
    # Schritt 1: Kaggle-Zugangsdaten prüfen
    if not kaggle_zugangsdaten_pruefen():
        sys.exit(1)
    
    # Schritt 2: Verzeichnisse einrichten
    rohdaten_verz, verarbeitete_daten_verz = verzeichnisse_einrichten()
    
    # Schritt 3: Datensatz herunterladen
    erfolg = datensatz_herunterladen(rohdaten_verz)
    
    if not erfolg:
        logger.error("Daten-Download fehlgeschlagen!")
        sys.exit(1)
    
    # Schritt 4: Dokumentation erstellen
    datenquellen_dokumentation_erstellen()
    
    logger.info("\n" + "="*60)
    logger.info("Datenanschaffung erfolgreich abgeschlossen!")
    logger.info("="*60)
    logger.info("\nNächste Schritte:")
    logger.info("1. Heruntergeladene Daten in raw_data/ überprüfen")
    logger.info("2. Datenwörterbuch erstellen")
    logger.info("3. Weiter zu Phase 3: Datenvorbereitung")


if __name__ == '__main__':
    main()
