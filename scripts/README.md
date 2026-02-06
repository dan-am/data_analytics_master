# Skripte-Verzeichnis

## Überblick
Dieses Verzeichnis enthält Hilfsskripte und wiederverwendbare Funktionen für das gesamte Projekt.

## Empfohlene Skripte

### Datenverarbeitung
- `data_loader.py` – Funktionen zum Laden und Validieren von Daten
- `data_transformer.py` – Häufige Datentransformationen
- `feature_utils.py` – Hilfsfunktionen für Feature Engineering

### Visualisierung
- `plotting_utils.py` – Wiederverwendbare Plot-Funktionen
- `reporting.py` – Berichtserstellungsfunktionen

### Modell-Hilfsfunktionen
- `model_utils.py` – Helfer für Modelltraining und -evaluation
- `metrics.py` – Benutzerdefinierte Metriken und Evaluationsfunktionen

### Allgemeine Hilfsfunktionen
- `config.py` – Konfiguration und Konstanten
- `logger.py` – Logging-Hilfsfunktionen
- `file_utils.py` – Datei-I/O-Helfer

## Beispiel: config.py

```python
"""
Projektkonfiguration und Konstanten
"""

from pathlib import Path

# Projektpfade
PROJEKT_ROOT = Path(__file__).parent.parent
DATEN_VERZEICHNIS = PROJEKT_ROOT / '2_data_acquisition'
ROHDATEN_VERZEICHNIS = DATEN_VERZEICHNIS / 'raw_data'
VERARBEITETE_DATEN_VERZEICHNIS = DATEN_VERZEICHNIS / 'processed_data'
MODELLE_VERZEICHNIS = PROJEKT_ROOT / 'models'
BERICHTE_VERZEICHNIS = PROJEKT_ROOT / 'reports'

# Modellparameter
ZUFALLS_SEED = 42
TEST_GROESSE = 0.2
KV_FALTEN = 5

# Feature-Listen (nach tatsächlichen Daten aktualisieren)
NUMERISCHE_FEATURES = []
KATEGORISCHE_FEATURES = []
ZIEL_SPALTE = 'segment'
```

## Beispiel: plotting_utils.py

```python
"""
Wiederverwendbare Plot-Funktionen
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_verteilung(daten, spalte, titel=None, speicher_pfad=None):
    """Verteilung einer Variable plotten."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Histogramm
    ax1.hist(daten[spalte], bins=30, edgecolor='black')
    ax1.set_xlabel(spalte)
    ax1.set_ylabel('Häufigkeit')
    ax1.set_title(f'Verteilung von {spalte}')
    
    # Boxplot
    ax2.boxplot(daten[spalte])
    ax2.set_ylabel(spalte)
    ax2.set_title(f'Boxplot von {spalte}')
    
    if titel:
        fig.suptitle(titel)
    
    plt.tight_layout()
    
    if speicher_pfad:
        plt.savefig(speicher_pfad, dpi=300, bbox_inches='tight')
    
    plt.show()

def plot_korrelationsmatrix(daten, titel='Korrelationsmatrix', speicher_pfad=None):
    """Korrelations-Heatmap plotten."""
    plt.figure(figsize=(10, 8))
    korrelation = daten.corr()
    sns.heatmap(korrelation, annot=True, cmap='coolwarm', center=0,
                fmt='.2f', square=True, linewidths=0.5)
    plt.title(titel)
    
    if speicher_pfad:
        plt.savefig(speicher_pfad, dpi=300, bbox_inches='tight')
    
    plt.show()
```

## Best Practices

1. **Modularität:** Jedes Skript hat einen klaren, einzelnen Zweck
2. **Dokumentation:** Docstrings für alle Funktionen
3. **Tests:** Unit-Tests für Hilfsfunktionen schreiben
4. **Imports:** Imports organisiert und minimal halten
5. **Wiederverwendbarkeit:** Allgemein einsetzbare Funktionen schreiben
6. **Konfiguration:** config.py für Konstanten nutzen

## Verwendung

Skripte in Notebooks oder anderen Skripten importieren:

```python
import sys
sys.path.append('../scripts')

from config import *
from plotting_utils import plot_verteilung
from data_loader import lade_bereinigte_daten
```
