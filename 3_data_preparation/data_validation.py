"""
Datenvalidierungsskript
Phase 3: Datenvorbereitung

Dieses Skript validiert die Qualität des Patientensegmentierungs-Datensatzes.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DatenValidator:
    """Klasse zur Validierung der Datenqualität."""
    
    def __init__(self, daten_pfad):
        """DatenValidator initialisieren."""
        self.daten_pfad = Path(daten_pfad)
        self.df = None
        self.validierungsergebnisse = {}
        
    def daten_laden(self):
        """Daten laden."""
        logger.info(f"Lade Daten von {self.daten_pfad}")
        self.df = pd.read_csv(self.daten_pfad)
        
    def vollstaendigkeit_validieren(self):
        """Datenvollständigkeit prüfen."""
        gesamt_zellen = self.df.shape[0] * self.df.shape[1]
        fehlende_zellen = self.df.isnull().sum().sum()
        vollstaendigkeit = ((gesamt_zellen - fehlende_zellen) / gesamt_zellen) * 100
        
        self.validierungsergebnisse['vollstaendigkeit'] = vollstaendigkeit
        logger.info(f"Datenvollständigkeit: {vollstaendigkeit:.2f}%")
        
        return vollstaendigkeit >= 95  # Bestanden wenn >= 95% vollständig
    
    def eindeutigkeit_validieren(self, id_spalte=None):
        """Auf doppelte Datensätze prüfen."""
        duplikate = self.df.duplicated().sum()
        self.validierungsergebnisse['duplikate'] = duplikate
        
        if duplikate > 0:
            logger.warning(f"{duplikate} doppelte Datensätze gefunden")
            return False
        else:
            logger.info("Keine doppelten Datensätze gefunden ✓")
            return True
    
    def datentypen_validieren(self):
        """Konsistenz der Datentypen validieren."""
        logger.info("Datentypen:")
        for spalte, dtyp in self.df.dtypes.items():
            logger.info(f"  {spalte}: {dtyp}")
        
        self.validierungsergebnisse['datentypen'] = self.df.dtypes.to_dict()
        return True
    
    def wertebereiche_validieren(self, bereichsregeln=None):
        """
        Prüfen, ob Werte innerhalb erwarteter Bereiche liegen.
        
        Args:
            bereichsregeln (dict): Wörterbuch mit Spalte: (min, max) Regeln
        """
        if bereichsregeln is None:
            bereichsregeln = {}
        
        verletzungen = []
        
        for spalte, (min_wert, max_wert) in bereichsregeln.items():
            if spalte in self.df.columns:
                ausserhalb = ((self.df[spalte] < min_wert) | (self.df[spalte] > max_wert)).sum()
                if ausserhalb > 0:
                    verletzungen.append(f"{spalte}: {ausserhalb} Werte außerhalb des Bereichs [{min_wert}, {max_wert}]")
        
        self.validierungsergebnisse['bereichsverletzungen'] = verletzungen
        
        if verletzungen:
            logger.warning("Bereichsvalidierungs-Verletzungen:")
            for v in verletzungen:
                logger.warning(f"  {v}")
            return False
        else:
            logger.info("Alle Werte innerhalb erwarteter Bereiche ✓")
            return True
    
    def validierungsbericht_erstellen(self):
        """Validierungsbericht erstellen."""
        bericht_pfad = self.daten_pfad.parent / 'validation_report.txt'
        
        with open(bericht_pfad, 'w') as f:
            f.write("Datenvalidierungsbericht\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Datensatz: {self.daten_pfad.name}\n")
            f.write(f"Zeilen: {self.df.shape[0]}\n")
            f.write(f"Spalten: {self.df.shape[1]}\n\n")
            
            for schluessel, wert in self.validierungsergebnisse.items():
                f.write(f"{schluessel}: {wert}\n")
        
        logger.info(f"Validierungsbericht gespeichert unter {bericht_pfad}")
    
    def validieren(self, bereichsregeln=None):
        """Alle Validierungsprüfungen durchführen."""
        self.daten_laden()
        
        ergebnisse = {
            'vollstaendigkeit': self.vollstaendigkeit_validieren(),
            'eindeutigkeit': self.eindeutigkeit_validieren(),
            'datentypen': self.datentypen_validieren(),
            'bereiche': self.wertebereiche_validieren(bereichsregeln)
        }
        
        self.validierungsbericht_erstellen()
        
        if all(ergebnisse.values()):
            logger.info("\n✓ Alle Validierungsprüfungen bestanden!")
            return True
        else:
            logger.warning("\n✗ Einige Validierungsprüfungen fehlgeschlagen")
            return False


def main():
    """Hauptfunktion zur Datenvalidierung."""
    basis_verz = Path(__file__).parent
    daten_datei = basis_verz.parent / '2_data_acquisition' / 'processed_data' / 'patient_data_cleaned.csv'
    
    if not daten_datei.exists():
        logger.error(f"Datendatei nicht gefunden: {daten_datei}")
        logger.error("Bitte zuerst data_cleaning.py ausführen")
        return
    
    validator = DatenValidator(daten_datei)
    
    # Validierungsregeln definieren (nach Bedarf anpassen)
    bereichsregeln = {
        # Beispiel: 'alter': (0, 120),
        # Beispiel: 'blutdruck': (60, 200),
    }
    
    validator.validieren(bereichsregeln=bereichsregeln)


if __name__ == '__main__':
    main()
