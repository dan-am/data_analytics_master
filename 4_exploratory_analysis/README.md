# Phase 4: Exploratory Data Analysis

## Overview
This phase focuses on understanding the data through statistical analysis and visualization.

## Objectives
- Understand data distributions
- Identify patterns and relationships
- Discover insights
- Visualize key features
- Generate statistical summaries

## Recommended Analyses

### Univariate Analysis
- **Numerical Variables:**
  - Distribution plots (histograms, KDE)
  - Box plots for outlier detection
  - Summary statistics (mean, median, std, quartiles)
  
- **Categorical Variables:**
  - Frequency counts
  - Bar charts
  - Pie charts for proportions

### Bivariate Analysis
- Correlation analysis (correlation matrix, heatmap)
- Scatter plots for numerical pairs
- Box plots for categorical vs numerical
- Cross-tabulations for categorical pairs

### Multivariate Analysis
- Pair plots
- Principal Component Analysis (PCA)
- Cluster tendency analysis

## Suggested Notebook Structure

```python
# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Data
df = pd.read_csv('../2_data_acquisition/processed_data/patient_data_cleaned.csv')

# 3. Basic Information
print(df.info())
print(df.describe())
print(df.head())

# 4. Univariate Analysis
# For each numerical column
for col in numerical_cols:
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    df[col].hist(bins=30)
    plt.subplot(1, 2, 2)
    df.boxplot(column=col)
    plt.show()

# 5. Correlation Analysis
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# 6. Bivariate Analysis
sns.pairplot(df)
plt.show()

# 7. Key Insights Documentation
```

## Visualization Guidelines

### Use appropriate chart types:
- **Distributions:** Histograms, KDE plots
- **Comparisons:** Bar charts, box plots
- **Relationships:** Scatter plots, line charts
- **Compositions:** Pie charts, stacked bar charts
- **Trends over time:** Line charts

### Best Practices:
- Clear titles and labels
- Appropriate color schemes
- Readable font sizes
- Consistent styling
- Annotations for key insights

## Key Questions to Answer

1. **Data Understanding:**
   - What is the shape of the data?
   - What types of variables do we have?
   - Are there any missing patterns?

2. **Distributions:**
   - Are numerical variables normally distributed?
   - Are there any skewed distributions?
   - What are the typical value ranges?

3. **Relationships:**
   - Which variables are correlated?
   - Are there any clusters in the data?
   - What patterns emerge?

4. **Patient Segments:**
   - Can we see natural groupings?
   - What features differentiate patients?
   - How many segments might exist?

## Tools and Libraries

```python
# Core data analysis
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Statistical analysis
from scipy import stats
from statsmodels.graphics.gofplots import qqplot

# Profiling (optional)
# from pandas_profiling import ProfileReport
```

## Deliverables

- [ ] EDA Jupyter notebook with comprehensive analysis
- [ ] Key visualizations saved as images
- [ ] Statistical summary report
- [ ] Initial insights document
- [ ] Recommendations for feature engineering

## Next Steps

After EDA:
1. Document key findings
2. Identify features for engineering
3. Determine modeling approach
4. Proceed to Phase 5: Feature Engineering
