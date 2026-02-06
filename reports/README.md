# Reports Directory

## Overview
This directory contains generated reports, visualizations, and documentation from the analysis.

## Report Types

### Analysis Reports
- `data_quality_report.html` - Data quality assessment
- `eda_report.html` - Exploratory data analysis findings
- `statistical_summary.pdf` - Statistical analysis results

### Model Reports
- `model_performance_report.pdf` - Model evaluation results
- `segment_profiles.pdf` - Patient segment characteristics
- `model_comparison.xlsx` - Comparison of different models

### Visualizations
- `segment_distribution.png` - Patient distribution across segments
- `feature_importance.png` - Important features for segmentation
- `cluster_visualization.png` - 2D visualization of clusters
- `correlation_heatmap.png` - Feature correlation matrix

## Generating Reports

### Using Pandas Profiling
```python
from pandas_profiling import ProfileReport

df = pd.read_csv('../2_data_acquisition/processed_data/patient_data_cleaned.csv')
profile = ProfileReport(df, title='Patient Data Profile')
profile.to_file('reports/data_quality_report.html')
```

### Creating PDF Reports
```python
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('reports/eda_visualizations.pdf') as pdf:
    # Create multiple plots
    fig1 = plt.figure()
    # ... plot code ...
    pdf.savefig(fig1)
    
    fig2 = plt.figure()
    # ... plot code ...
    pdf.savefig(fig2)
```

### Excel Reports
```python
with pd.ExcelWriter('reports/analysis_results.xlsx') as writer:
    df_summary.to_excel(writer, sheet_name='Summary')
    df_segments.to_excel(writer, sheet_name='Segments')
    df_metrics.to_excel(writer, sheet_name='Metrics')
```

## Best Practices

1. **Naming:** Use descriptive names with dates if versioning
2. **Format:** Choose appropriate format (HTML for interactive, PDF for distribution)
3. **Documentation:** Include context and interpretation
4. **Version Control:** Don't commit large binary files; use .gitignore
5. **Organization:** Group related reports together

## Report Checklist

- [ ] Executive summary included
- [ ] Key findings highlighted
- [ ] Visualizations are clear and labeled
- [ ] Methodology documented
- [ ] Recommendations provided
- [ ] Date and version noted
