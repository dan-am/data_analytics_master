"""
Datenbereinigungsskript
Phase 3: Datenvorbereitung

Dieses Skript führt Datenbereinigungsoperationen auf dem Patientensegmentierungs-Datensatz durch.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

# Logging einrichten
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DatenBereiniger:
    """Klasse zur Durchführung von Datenbereinigungsoperationen."""
    
    def __init__(self, eingabe_pfad, ausgabe_pfad):
        """
        DatenBereiniger initialisieren.
        
        Args:
            eingabe_pfad (str): Pfad zur Rohdatendatei
            ausgabe_pfad (str): Pfad zum Speichern der bereinigten Daten
        """
        self.eingabe_pfad = Path(eingabe_pfad)
        self.ausgabe_pfad = Path(ausgabe_pfad)
        self.df = None
        self.bereinigungsbericht = []
        
    def daten_laden(self):
        """Rohdaten laden."""
        logger.info(f"Lade Daten von {self.eingabe_pfad}")
        self.df = pd.read_csv(self.eingabe_pfad)
        logger.info(f"Daten geladen: {self.df.shape[0]} Zeilen, {self.df.shape[1]} Spalten")
        self.bereinigungsbericht.append(f"Ursprüngliche Form: {self.df.shape}")
        
    def duplikate_pruefen(self):
        """Doppelte Zeilen identifizieren und entfernen."""
        duplikate = self.df.duplicated().sum()
        
        if duplikate > 0:
            logger.warning(f"{duplikate} doppelte Zeilen gefunden")
            self.df = self.df.drop_duplicates()
            logger.info(f"{duplikate} doppelte Zeilen entfernt")
            self.bereinigungsbericht.append(f"Duplikate entfernt: {duplikate}")
        else:
            logger.info("Keine doppelten Zeilen gefunden")
            self.bereinigungsbericht.append("Keine Duplikate gefunden")
    
    def fehlende_werte_behandeln(self, strategie='analysieren'):
        """
        Fehlende Werte im Datensatz behandeln.
        
        Args:
            strategie (str): Strategie zur Behandlung fehlender Werte
                           'analysieren' - nur fehlende Werte melden
                           'entfernen' - Zeilen mit fehlenden Werten entfernen
                           'imputieren' - fehlende Werte imputieren
        """
        fehlend = self.df.isnull().sum()
        fehlend_proz = (fehlend / len(self.df)) * 100
        
        if fehlend.sum() > 0:
            logger.info("Fehlende Werte gefunden:")
            for spalte, anzahl in fehlend[fehlend > 0].items():
                logger.info(f"  {spalte}: {anzahl} ({fehlend_proz[spalte]:.2f}%)")
                self.bereinigungsbericht.append(f"Fehlend in {spalte}: {anzahl} ({fehlend_proz[spalte]:.2f}%)")
            
            if strategie == 'entfernen':
                anfangs_anzahl = len(self.df)
                self.df = self.df.dropna()
                entfernt = anfangs_anzahl - len(self.df)
                logger.info(f"{entfernt} Zeilen mit fehlenden Werten entfernt")
                self.bereinigungsbericht.append(f"Entfernte Zeilen (fehlende Werte): {entfernt}")
            
            elif strategie == 'imputieren':
                # Numerische Spalten mit Median imputieren
                num_spalten = self.df.select_dtypes(include=[np.number]).columns
                for spalte in num_spalten:
                    if self.df[spalte].isnull().any():
                        median_wert = self.df[spalte].median()
                        self.df[spalte].fillna(median_wert, inplace=True)
                        logger.info(f"{spalte} mit Median imputiert: {median_wert}")
                
                # Kategorische Spalten mit Modus imputieren
                kat_spalten = self.df.select_dtypes(include=['object']).columns
                for spalte in kat_spalten:
                    if self.df[spalte].isnull().any():
                        modus_wert = self.df[spalte].mode()[0]
                        self.df[spalte].fillna(modus_wert, inplace=True)
                        logger.info(f"{spalte} mit Modus imputiert: {modus_wert}")
                
                self.bereinigungsbericht.append("Fehlende Werte imputiert")
        else:
            logger.info("Keine fehlenden Werte gefunden")
            self.bereinigungsbericht.append("Keine fehlenden Werte")
    
    def ausreisser_erkennen(self, methode='iqr'):
        """
        Ausreißer in numerischen Spalten erkennen.
        
        Args:
            methode (str): Methode zur Ausreißererkennung ('iqr' oder 'zscore')
        """
        num_spalten = self.df.select_dtypes(include=[np.number]).columns
        
        logger.info(f"Erkenne Ausreißer mit {methode}-Methode")
        
        for spalte in num_spalten:
            if methode == 'iqr':
                Q1 = self.df[spalte].quantile(0.25)
                Q3 = self.df[spalte].quantile(0.75)
                IQR = Q3 - Q1
                untere_grenze = Q1 - 1.5 * IQR
                obere_grenze = Q3 + 1.5 * IQR
                ausreisser = ((self.df[spalte] < untere_grenze) | (self.df[spalte] > obere_grenze)).sum()
                
            elif methode == 'zscore':
                z_werte = np.abs((self.df[spalte] - self.df[spalte].mean()) / self.df[spalte].std())
                ausreisser = (z_werte > 3).sum()
            
            if ausreisser > 0:
                proz = (ausreisser / len(self.df)) * 100
                logger.info(f"  {spalte}: {ausreisser} Ausreißer ({proz:.2f}%)")
                self.bereinigungsbericht.append(f"Ausreißer in {spalte}: {ausreisser} ({proz:.2f}%)")
    
    def spaltennamen_standardisieren(self):
        """Spaltennamen standardisieren (Kleinbuchstaben, Unterstriche)."""
        original_spalten = self.df.columns.tolist()
        self.df.columns = self.df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')
        neue_spalten = self.df.columns.tolist()
        
        if original_spalten != neue_spalten:
            logger.info("Spaltennamen standardisiert")
            self.bereinigungsbericht.append("Spaltennamen standardisiert")
    
    def bereinigte_daten_speichern(self):
        """Bereinigten Datensatz speichern."""
        self.ausgabe_pfad.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(self.ausgabe_pfad, index=False)
        logger.info(f"Bereinigte Daten gespeichert unter {self.ausgabe_pfad}")
        logger.info(f"Endgültige Form: {self.df.shape[0]} Zeilen, {self.df.shape[1]} Spalten")
        self.bereinigungsbericht.append(f"Endgültige Form: {self.df.shape}")
    
    def bericht_erstellen(self):
        """Bereinigungsbericht erstellen."""
        bericht_pfad = self.ausgabe_pfad.parent / 'cleaning_report.txt'
        
        with open(bericht_pfad, 'w') as f:
            f.write("Datenbereinigungsbericht\n")
            f.write("=" * 50 + "\n\n")
            for eintrag in self.bereinigungsbericht:
                f.write(f"{eintrag}\n")
        
        logger.info(f"Bereinigungsbericht gespeichert unter {bericht_pfad}")
        
    def bereinigen(self, fehlend_strategie='analysieren', ausreisser_entfernen=False):
        """
        Vollständige Bereinigungs-Pipeline ausführen.
        
        Args:
            fehlend_strategie (str): Strategie zur Behandlung fehlender Werte
            ausreisser_entfernen (bool): Ob Ausreißer entfernt werden sollen
        """
        self.daten_laden()
        self.spaltennamen_standardisieren()
        self.duplikate_pruefen()
        self.fehlende_werte_behandeln(strategie=fehlend_strategie)
        self.ausreisser_erkennen()
        self.bereinigte_daten_speichern()
        self.bericht_erstellen()
        
        logger.info("Datenbereinigung abgeschlossen!")


def main():
    """Hauptfunktion zur Datenbereinigung."""
    # Pfade definieren (bei Bedarf anpassen)
    basis_verz = Path(__file__).parent
    eingabe_datei = basis_verz.parent / '2_data_acquisition' / 'raw_data' / 'patient_data.csv'
    ausgabe_datei = basis_verz.parent / '2_data_acquisition' / 'processed_data' / 'patient_data_cleaned.csv'
    
    # Prüfen, ob Eingabedatei existiert
    if not eingabe_datei.exists():
        logger.error(f"Eingabedatei nicht gefunden: {eingabe_datei}")
        logger.error("Bitte zuerst das Datenanschaffungs-Skript ausführen")
        logger.error("Oder den eingabe_datei-Pfad in diesem Skript anpassen")
        return
    
    # Bereiniger erstellen und Bereinigung durchführen
    bereiniger = DatenBereiniger(eingabe_datei, ausgabe_datei)
    bereiniger.bereinigen(fehlend_strategie='imputieren', ausreisser_entfernen=False)


if __name__ == '__main__':
    main()
