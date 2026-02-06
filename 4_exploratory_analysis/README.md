# Phase 4: Explorative Datenanalyse

## Überblick
Diese Phase konzentriert sich auf das Verständnis der Daten durch statistische Analysen und Visualisierungen.

## Ziele
- Datenverteilungen verstehen
- Muster und Zusammenhänge identifizieren
- Erkenntnisse gewinnen
- Wichtige Features visualisieren
- Statistische Zusammenfassungen erstellen

## Empfohlene Analysen

### Univariate Analyse
- **Numerische Variablen:**
  - Verteilungsdiagramme (Histogramme, KDE)
  - Boxplots zur Ausreißererkennung
  - Zusammenfassende Statistiken (Mittelwert, Median, Std, Quartile)
  
- **Kategorische Variablen:**
  - Häufigkeitsverteilungen
  - Balkendiagramme
  - Kreisdiagramme für Anteile

### Bivariate Analyse
- Korrelationsanalyse (Korrelationsmatrix, Heatmap)
- Streudiagramme für numerische Paare
- Boxplots für kategorisch vs. numerisch
- Kreuztabellen für kategorische Paare

### Multivariate Analyse
- Pairplots
- Hauptkomponentenanalyse (PCA)
- Cluster-Tendenz-Analyse

## Vorgeschlagene Notebook-Struktur

```python
# 1. Bibliotheken importieren
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Daten laden
df = pd.read_csv('../2_data_acquisition/processed_data/patient_data_cleaned.csv')

# 3. Basisinformationen
print(df.info())
print(df.describe())
print(df.head())

# 4. Univariate Analyse
for col in numerical_cols:
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    df[col].hist(bins=30)
    plt.subplot(1, 2, 2)
    df.boxplot(column=col)
    plt.show()

# 5. Korrelationsanalyse
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# 6. Bivariate Analyse
sns.pairplot(df)
plt.show()

# 7. Wichtige Erkenntnisse dokumentieren
```

## Visualisierungsrichtlinien

### Geeignete Diagrammtypen verwenden:
- **Verteilungen:** Histogramme, KDE-Plots
- **Vergleiche:** Balkendiagramme, Boxplots
- **Zusammenhänge:** Streudiagramme, Liniendiagramme
- **Zusammensetzungen:** Kreisdiagramme, gestapelte Balkendiagramme
- **Zeitliche Trends:** Liniendiagramme

### Best Practices:
- Klare Titel und Beschriftungen
- Geeignete Farbschemata
- Lesbare Schriftgrößen
- Einheitliches Styling
- Annotationen für wichtige Erkenntnisse

## Zentrale Fragen

1. **Datenverständnis:**
   - Welche Form haben die Daten?
   - Welche Variablentypen gibt es?
   - Gibt es fehlende Datenmuster?

2. **Verteilungen:**
   - Sind numerische Variablen normalverteilt?
   - Gibt es schiefe Verteilungen?
   - Was sind die typischen Wertebereiche?

3. **Zusammenhänge:**
   - Welche Variablen korrelieren?
   - Gibt es Cluster in den Daten?
   - Welche Muster zeichnen sich ab?

4. **Patientensegmente:**
   - Sind natürliche Gruppierungen erkennbar?
   - Welche Features unterscheiden die Patienten?
   - Wie viele Segmente könnten existieren?

## Ergebnisse

- [ ] EDA-Jupyter-Notebook mit umfassender Analyse
- [ ] Wichtige Visualisierungen als Bilder gespeichert
- [ ] Statistischer Zusammenfassungsbericht
- [ ] Dokument mit ersten Erkenntnissen
- [ ] Empfehlungen für Feature Engineering

## Nächste Schritte

Nach der EDA:
1. Wichtige Ergebnisse dokumentieren
2. Features für das Engineering identifizieren
3. Modellierungsansatz festlegen
4. Weiter zu Phase 5: Feature Engineering
