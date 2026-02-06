# Notebooks-Verzeichnis

## Überblick
Dieses Verzeichnis enthält Jupyter-Notebooks für interaktive Analysen und Experimente.

### Notebook-Struktur

#### Datenexploration
- `01_erste_datenexploration.ipynb` – Erster Blick auf die Daten
- `02_eda_umfassend.ipynb` – Umfassende explorative Datenanalyse
- `03_statistische_analyse.ipynb` – Statistische Tests und Analysen

#### Feature Engineering
- `04_feature_erstellung.ipynb` – Experimente mit neuen Features
- `05_feature_selektion.ipynb` – Feature-Selektions-Experimente

#### Modellierung
- `06_baseline_modelle.ipynb` – Baseline-Modell-Experimente
- `07_modell_tuning.ipynb` – Hyperparameter-Tuning
- `08_modellvergleich.ipynb` – Vergleich verschiedener Ansätze

#### Evaluation
- `09_modellevaluation.ipynb` – Endgültige Modellevaluation
- `10_segmentanalyse.ipynb` – Detaillierte Segmentanalyse

## Best Practices

1. **Namenskonvention:** Nummerierung für Reihenfolge, beschreibende Namen
2. **Klare Struktur:** Markdown-Überschriften, Kommentare, nachvollziehbare Ergebnisse
3. **Versionskontrolle:** Notebooks mit gelöschten Ausgaben committen
4. **Reproduzierbarkeit:** Zufallsseeds setzen, Versionen dokumentieren
5. **Dokumentation:** Analyseentscheidungen und Ergebnisse festhalten

## Notebook-Vorlage

```python
# Titel: [Notebook-Zweck]
# Autor: [Name]
# Datum: [Datum]
# Beschreibung: [Kurzbeschreibung]

# 1. Setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Zufallsseed setzen
np.random.seed(42)

# Plot-Stil festlegen
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# 2. Daten laden
# [Code hier]

# 3. Analyse
# [Code hier]

# 4. Ergebnisse
# [Erkenntnisse dokumentieren]
```

## Tipps

- Markdown-Zellen verwenden, um Gedankengänge zu erklären
- Visualisierungen zur Unterstützung der Ergebnisse einbinden
- Wichtige Plots im reports/-Verzeichnis speichern
- Ausgaben vor dem Committen löschen
- Notebooks auf bestimmte Aufgaben fokussieren
