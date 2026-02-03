# Phase 3: Data Preparation

## Overview
This phase focuses on cleaning and preparing the patient data for analysis.

## Objectives
- Clean raw data
- Handle missing values
- Detect and treat outliers
- Validate data quality
- Create preprocessing pipeline

## Scripts

### 1. data_cleaning.py
Performs comprehensive data cleaning:
- Removes duplicates
- Handles missing values
- Detects outliers
- Standardizes column names
- Generates cleaning report

**Usage:**
```python
python data_cleaning.py
```

### 2. data_validation.py
Validates data quality:
- Checks completeness
- Validates uniqueness
- Verifies data types
- Validates value ranges
- Generates validation report

**Usage:**
```python
python data_validation.py
```

### 3. preprocessing_pipeline.py
Complete preprocessing pipeline for reproducibility

## Data Quality Checklist

### Completeness
- [ ] All required columns present
- [ ] Missing value percentage < 5%
- [ ] No entire columns/rows missing

### Consistency
- [ ] Data types are correct
- [ ] No duplicate records
- [ ] Column names standardized
- [ ] Date formats consistent

### Validity
- [ ] Values within expected ranges
- [ ] No impossible values (e.g., negative age)
- [ ] Categorical values are valid
- [ ] ID fields are unique

### Accuracy
- [ ] Statistical summaries are reasonable
- [ ] No obvious data entry errors
- [ ] Cross-field validation passes

## Common Data Issues and Solutions

### Missing Values
- **Detection:** Use `df.isnull().sum()`
- **Strategies:**
  - Drop if < 5% of data
  - Impute with mean/median/mode
  - Use advanced imputation (KNN, MICE)
  - Create 'missing' indicator

### Duplicates
- **Detection:** Use `df.duplicated()`
- **Action:** Remove using `df.drop_duplicates()`
- **Consider:** Partial duplicates on key fields

### Outliers
- **Detection Methods:**
  - IQR method (1.5 * IQR)
  - Z-score (> 3 standard deviations)
  - Domain knowledge
- **Treatment:**
  - Remove if data errors
  - Cap/floor (winsorization)
  - Transform (log, sqrt)
  - Keep if valid extreme values

### Data Types
- **Issues:** Numeric stored as string, dates as object
- **Solution:** Convert using `pd.to_numeric()`, `pd.to_datetime()`

## Output Files

- `processed_data/patient_data_cleaned.csv` - Cleaned dataset
- `cleaning_report.txt` - Cleaning operations log
- `validation_report.txt` - Data quality validation results

## Best Practices

1. **Never modify raw data** - Always create new files
2. **Document all changes** - Keep track of cleaning decisions
3. **Version control** - Track changes to processing scripts
4. **Reproducibility** - Make pipeline re-runnable
5. **Validation** - Always validate after cleaning

## Next Steps

After data preparation:
1. Review cleaning and validation reports
2. Verify data quality meets requirements
3. Proceed to Phase 4: Exploratory Data Analysis

## Notes

- Keep raw data unchanged in `2_data_acquisition/raw_data/`
- Save processed data to `2_data_acquisition/processed_data/`
- Document all preprocessing decisions
- Consider creating data lineage documentation
