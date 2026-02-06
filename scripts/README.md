# Scripts Directory

## Overview
This directory contains utility scripts and helper functions used across the project.

## Recommended Scripts

### Data Processing
- `data_loader.py` - Functions to load and validate data
- `data_transformer.py` - Common data transformations
- `feature_utils.py` - Feature engineering utilities

### Visualization
- `plotting_utils.py` - Reusable plotting functions
- `reporting.py` - Report generation utilities

### Model Utilities
- `model_utils.py` - Model training and evaluation helpers
- `metrics.py` - Custom metrics and evaluation functions

### General Utilities
- `config.py` - Configuration and constants
- `logger.py` - Logging utilities
- `file_utils.py` - File I/O helpers

## Example: config.py

```python
"""
Project configuration and constants
"""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / '2_data_acquisition'
RAW_DATA_DIR = DATA_DIR / 'raw_data'
PROCESSED_DATA_DIR = DATA_DIR / 'processed_data'
MODELS_DIR = PROJECT_ROOT / 'models'
REPORTS_DIR = PROJECT_ROOT / 'reports'

# Model parameters
RANDOM_SEED = 42
TEST_SIZE = 0.2
CV_FOLDS = 5

# Feature lists (to be updated based on actual data)
NUMERICAL_FEATURES = []
CATEGORICAL_FEATURES = []
TARGET_COLUMN = 'segment'

# Model configurations
KMEANS_CONFIG = {
    'n_clusters': 4,
    'random_state': RANDOM_SEED,
    'n_init': 10
}

RANDOM_FOREST_CONFIG = {
    'n_estimators': 100,
    'max_depth': 10,
    'random_state': RANDOM_SEED
}
```

## Example: plotting_utils.py

```python
"""
Reusable plotting functions
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(data, column, title=None, save_path=None):
    """Plot distribution of a variable."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Histogram
    ax1.hist(data[column], bins=30, edgecolor='black')
    ax1.set_xlabel(column)
    ax1.set_ylabel('Frequency')
    ax1.set_title(f'Distribution of {column}')
    
    # Box plot
    ax2.boxplot(data[column])
    ax2.set_ylabel(column)
    ax2.set_title(f'Box Plot of {column}')
    
    if title:
        fig.suptitle(title)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()

def plot_correlation_matrix(data, title='Correlation Matrix', save_path=None):
    """Plot correlation heatmap."""
    plt.figure(figsize=(10, 8))
    correlation = data.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0,
                fmt='.2f', square=True, linewidths=0.5)
    plt.title(title)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
```

## Best Practices

1. **Modularity:** Each script should have a single, clear purpose
2. **Documentation:** Include docstrings for all functions
3. **Testing:** Write unit tests for utility functions
4. **Imports:** Keep imports organized and minimal
5. **Reusability:** Write general-purpose functions
6. **Configuration:** Use config.py for constants

## Usage

Import scripts in notebooks or other scripts:

```python
import sys
sys.path.append('../scripts')

from config import *
from plotting_utils import plot_distribution
from data_loader import load_cleaned_data
```
