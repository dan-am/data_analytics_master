# Notebooks Directory

## Overview
This directory contains Jupyter notebooks for interactive analysis and experimentation.

## Recommended Notebooks

### 1. Data Exploration
- `01_initial_data_exploration.ipynb` - First look at the data
- `02_eda_comprehensive.ipynb` - Comprehensive exploratory data analysis
- `03_statistical_analysis.ipynb` - Statistical tests and analysis

### 2. Feature Engineering
- `04_feature_creation.ipynb` - Experimenting with new features
- `05_feature_selection.ipynb` - Feature selection experiments

### 3. Modeling
- `06_baseline_models.ipynb` - Baseline model experiments
- `07_model_tuning.ipynb` - Hyperparameter tuning
- `08_model_comparison.ipynb` - Compare different approaches

### 4. Evaluation
- `09_model_evaluation.ipynb` - Final model evaluation
- `10_segment_analysis.ipynb` - Deep dive into segments

## Best Practices

1. **Naming Convention:** Use numbers for ordering, descriptive names
2. **Clear Structure:** 
   - Markdown headers for sections
   - Comments explaining complex code
   - Clear outputs showing results
3. **Version Control:** Commit notebooks with outputs cleared
4. **Reproducibility:** Set random seeds, document versions
5. **Documentation:** Include analysis decisions and findings

## Notebook Template

```python
# Title: [Notebook Purpose]
# Author: [Your Name]
# Date: [Date]
# Description: [Brief description]

# 1. Setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed
np.random.seed(42)

# Set plotting style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# 2. Load Data
# [Your code]

# 3. Analysis
# [Your code]

# 4. Conclusions
# [Document findings]
```

## Tips

- Use markdown cells liberally to explain your thinking
- Include visualizations to support findings
- Save important plots to the reports/ directory
- Clear outputs before committing to git
- Keep notebooks focused on specific tasks
