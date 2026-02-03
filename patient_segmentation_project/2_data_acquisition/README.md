# Phase 2: Data Acquisition

## Overview
This phase focuses on collecting and organizing the patient segmentation dataset.

## Objectives
- Download the dataset from Kaggle
- Document the data source
- Organize raw data files
- Perform initial data assessment

## Dataset Information

**Source:** [Patient Segmentation Data](https://www.kaggle.com/datasets/nudratabbas/patient-segmentation-data)

**Provider:** Kaggle

**Author:** Nudrat Abbas

## Directory Structure

```
2_data_acquisition/
├── raw_data/              # Original, unmodified data files
├── processed_data/        # Cleaned and processed data
├── data_sources/          # Data source documentation
└── download_data.py       # Data download script
```

## Instructions

### Step 1: Setup Kaggle API

1. Create a Kaggle account at https://www.kaggle.com
2. Go to your account settings: https://www.kaggle.com/account
3. Scroll to "API" section
4. Click "Create New API Token"
5. This downloads `kaggle.json` file
6. Place the file in `~/.kaggle/` directory:

```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### Step 2: Install Dependencies

```bash
pip install kaggle
```

### Step 3: Download Dataset

Run the download script:

```bash
python download_data.py
```

This script will:
- Verify Kaggle credentials
- Create necessary directories
- Download the dataset
- Create documentation

### Step 4: Verify Download

After download, check the `raw_data/` directory:

```bash
ls -lh raw_data/
```

### Step 5: Initial Data Exploration

Quick preview of the data:

```python
import pandas as pd

# Load the data
df = pd.read_csv('raw_data/[filename].csv')

# Display basic info
print(df.info())
print(df.head())
print(df.describe())
```

## Data Quality Checklist

- [ ] Dataset downloaded successfully
- [ ] All expected files present
- [ ] File sizes are reasonable
- [ ] Data can be loaded without errors
- [ ] Data source documented
- [ ] Initial row/column counts recorded

## Data Documentation

Create a data dictionary in `data_sources/` folder documenting:
- Column names and descriptions
- Data types
- Expected value ranges
- Missing value indicators
- Any known data quality issues

## Next Steps

After completing data acquisition:
1. Review the data structure and contents
2. Document any initial observations
3. Proceed to Phase 3: Data Preparation

## Notes

- Keep raw data files in `raw_data/` unmodified
- All processing should create new files in `processed_data/`
- Document any data issues discovered
- Track data versions if multiple downloads occur

## Troubleshooting

**Issue:** Kaggle credentials not found
- **Solution:** Verify `~/.kaggle/kaggle.json` exists and has correct permissions

**Issue:** Dataset not found
- **Solution:** Verify the dataset name and that it's still available on Kaggle

**Issue:** Download fails
- **Solution:** Check internet connection and Kaggle API status

## References

- [Kaggle API Documentation](https://github.com/Kaggle/kaggle-api)
- [Dataset Page](https://www.kaggle.com/datasets/nudratabbas/patient-segmentation-data)
