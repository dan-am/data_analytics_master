# Phase 3: Datenvorbereitung

## Überblick
Diese Phase konzentriert sich auf die Bereinigung und Aufbereitung der Patientendaten für die Analyse.

## Ziele
- Rohdaten bereinigen
- Fehlende Werte behandeln
- Ausreißer erkennen und behandeln
- Datenqualität validieren
- Vorverarbeitungs-Pipeline erstellen

## Skripte

### 1. data_cleaning.py
Führt eine umfassende Datenbereinigung durch:
- Duplikate entfernen
- Fehlende Werte behandeln
- Ausreißer erkennen
- Spaltennamen standardisieren
- Bereinigungsbericht erstellen

**Verwendung:**
```python
python data_cleaning.py
```

### 2. data_validation.py
Validiert die Datenqualität:
- Vollständigkeit prüfen
- Eindeutigkeit validieren
- Datentypen überprüfen
- Wertebereiche validieren
- Validierungsbericht erstellen

**Verwendung:**
```python
python data_validation.py
```

## Datenqualitäts-Checkliste

### Vollständigkeit
- [ ] Alle erforderlichen Spalten vorhanden
- [ ] Anteil fehlender Werte < 5 %
- [ ] Keine vollständig fehlenden Spalten/Zeilen

### Konsistenz
- [ ] Datentypen sind korrekt
- [ ] Keine doppelten Datensätze
- [ ] Spaltennamen standardisiert
- [ ] Datumsformate einheitlich

### Gültigkeit
- [ ] Werte innerhalb erwarteter Bereiche
- [ ] Keine unmöglichen Werte (z. B. negatives Alter)
- [ ] Kategorische Werte sind gültig
- [ ] ID-Felder sind eindeutig

### Genauigkeit
- [ ] Statistische Zusammenfassungen sind plausibel
- [ ] Keine offensichtlichen Eingabefehler
- [ ] Feldübergreifende Validierung bestanden

## Häufige Datenprobleme und Lösungen

### Fehlende Werte
- **Erkennung:** `df.isnull().sum()` verwenden
- **Strategien:**
  - Entfernen, wenn < 5 % der Daten betroffen
  - Mit Mittelwert/Median/Modus imputieren
  - Fortgeschrittene Imputation (KNN, MICE)
  - „Fehlend"-Indikator erstellen

### Duplikate
- **Erkennung:** `df.duplicated()` verwenden
- **Maßnahme:** Mit `df.drop_duplicates()` entfernen
- **Beachten:** Teilduplikate auf Schlüsselfeldern

### Ausreißer
- **Erkennungsmethoden:**
  - IQR-Methode (1,5 × IQR)
  - Z-Score (> 3 Standardabweichungen)
  - Fachwissen
- **Behandlung:**
  - Entfernen bei Datenfehlern
  - Begrenzen (Winsorisierung)
  - Transformieren (log, sqrt)
  - Beibehalten bei gültigen Extremwerten

### Datentypen
- **Probleme:** Numerische Werte als String gespeichert, Datumsangaben als Object
- **Lösung:** Konvertieren mit `pd.to_numeric()`, `pd.to_datetime()`

## Ausgabedateien

- `processed_data/patient_data_cleaned.csv` – Bereinigter Datensatz
- `cleaning_report.txt` – Protokoll der Bereinigungsschritte
- `validation_report.txt` – Ergebnisse der Datenqualitätsvalidierung

## Best Practices

1. **Rohdaten niemals ändern** – Immer neue Dateien erstellen
2. **Alle Änderungen dokumentieren** – Bereinigungsentscheidungen nachverfolgen
3. **Versionskontrolle** – Änderungen an Verarbeitungsskripten nachverfolgen
4. **Reproduzierbarkeit** – Pipeline wiederholbar gestalten
5. **Validierung** – Nach der Bereinigung immer validieren

## Nächste Schritte

Nach der Datenvorbereitung:
1. Bereinigungs- und Validierungsberichte überprüfen
2. Sicherstellen, dass die Datenqualität den Anforderungen entspricht
3. Weiter zu Phase 4: Explorative Datenanalyse
