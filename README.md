# Patient Segmentation Analysis Project

## Project Overview
This project implements a comprehensive data analytics workflow for patient segmentation using the [Patient Segmentation Dataset from Kaggle](https://www.kaggle.com/datasets/nudratabbas/patient-segmentation-data).
## 📚 Resources

### Dataset Recommendations
Looking for interesting datasets for your seminar paper? Check out our comprehensive guide:

**[Dataset Recommendations Guide](dataset_recommendations.md)** - Curated datasets for:
- 🔍 Clustering Analysis
- 🛒 Market Basket Analysis (Warenkorbanalyse)
- 💰 Financial Data & KYC Analysis
- 🎯 Classification Tasks

The guide focuses on less commonly used but comprehensive datasets suitable for academic work.

## Projects

## Data Science Life Cycle Phases

This project follows a structured approach based on the Data Science Life Cycle:

### Phase 1: Business Understanding
**Objective:** Define the business problem and project goals.
- **Folder:** `1_business_understanding/`
- **Purpose:** Understand patient segmentation needs for healthcare providers
- **Deliverables:** Problem definition, success criteria, project charter

### Phase 2: Data Acquisition
**Objective:** Collect and store relevant data.
- **Folder:** `2_data_acquisition/`
- **Purpose:** Download and organize the patient segmentation dataset
- **Deliverables:** Raw data files, data source documentation, download scripts

### Phase 3: Data Preparation
**Objective:** Clean and preprocess the data.
- **Folder:** `3_data_preparation/`
- **Purpose:** Handle missing values, outliers, and data quality issues
- **Deliverables:** Cleaned datasets, data quality reports, preprocessing scripts

### Phase 4: Exploratory Data Analysis (EDA)
**Objective:** Understand data patterns and relationships.
- **Folder:** `4_exploratory_analysis/`
- **Purpose:** Visualize distributions, correlations, and key insights
- **Deliverables:** EDA notebooks, visualization reports, statistical summaries

### Phase 5: Feature Engineering
**Objective:** Create and select relevant features.
- **Folder:** `5_feature_engineering/`
- **Purpose:** Engineer features for patient segmentation models
- **Deliverables:** Feature creation scripts, feature selection analysis

### Phase 6: Modeling
**Objective:** Build and train machine learning models.
- **Folder:** `6_modeling/`
- **Purpose:** Develop clustering/classification models for patient segmentation
- **Deliverables:** Trained models, model training scripts, hyperparameter tuning results

### Phase 7: Evaluation
**Objective:** Assess model performance.
- **Folder:** `7_evaluation/`
- **Purpose:** Evaluate segmentation quality and model metrics
- **Deliverables:** Evaluation reports, performance metrics, model comparison

### Phase 8: Deployment
**Objective:** Prepare for production deployment.
- **Folder:** `8_deployment/`
- **Purpose:** Document deployment strategy and create inference scripts
- **Deliverables:** Deployment guide, API specifications, monitoring plan

## Project Structure

```
patient_segmentation_project/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── 1_business_understanding/          # Business problem definition
│   ├── project_charter.md
│   └── success_criteria.md
├── 2_data_acquisition/                # Data collection
│   ├── raw_data/                      # Original datasets (gitignored)
│   ├── processed_data/                # Processed datasets (gitignored)
│   ├── data_sources/                  # Data source documentation
│   └── download_data.py               # Script to download data
├── 3_data_preparation/                # Data cleaning
│   ├── data_cleaning.py
│   ├── data_validation.py
│   └── preprocessing_pipeline.py
├── 4_exploratory_analysis/            # EDA
│   ├── eda_notebook.ipynb
│   ├── statistical_analysis.py
│   └── visualization.py
├── 5_feature_engineering/             # Feature creation
│   ├── feature_creation.py
│   ├── feature_selection.py
│   └── feature_engineering_pipeline.py
├── 6_modeling/                        # Model development
│   ├── train_model.py
│   ├── hyperparameter_tuning.py
│   └── clustering_models.py
├── 7_evaluation/                      # Model evaluation
│   ├── evaluate_model.py
│   ├── performance_metrics.py
│   └── model_comparison.py
├── 8_deployment/                      # Deployment
│   ├── deployment_guide.md
│   ├── inference_script.py
│   └── api_documentation.md
├── notebooks/                         # Jupyter notebooks
├── reports/                           # Generated analysis reports
├── scripts/                           # Utility scripts
├── models/                            # Saved model files (gitignored)
└── references/                        # Reference materials
```

## Getting Started

### Prerequisites
- Python 3.8+
- Kaggle account for data download
- Required Python packages (see requirements.txt)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/dan-am/data_analytics_master.git
cd data_analytics_master/patient_segmentation_project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Kaggle API credentials:
   - Create a Kaggle account at https://www.kaggle.com
   - Go to Account settings → API → Create New API Token
   - Place the downloaded `kaggle.json` in `~/.kaggle/`

4. Download the dataset:
```bash
python 2_data_acquisition/download_data.py
```

### Usage

Follow the phases in order:

1. **Review Business Understanding:** Read documentation in `1_business_understanding/`
2. **Acquire Data:** Run data download script in `2_data_acquisition/`
3. **Prepare Data:** Execute cleaning scripts in `3_data_preparation/`
4. **Explore Data:** Run EDA notebooks in `4_exploratory_analysis/`
5. **Engineer Features:** Create features using `5_feature_engineering/` scripts
6. **Build Models:** Train models with scripts in `6_modeling/`
7. **Evaluate:** Assess performance using `7_evaluation/` scripts
8. **Deploy:** Follow deployment guide in `8_deployment/`

## Dataset Information

**Source:** [Kaggle - Patient Segmentation Data](https://www.kaggle.com/datasets/nudratabbas/patient-segmentation-data)

**Description:** This dataset contains patient information for segmentation analysis, useful for healthcare analytics and patient clustering.

## Contributing

Contributions are welcome! Please follow the established project structure and Data Science Life Cycle phases.

## License

This project is part of the DAMI01/DATA01 Data Analytics Masters course.

## Contact

For questions or issues, please open an issue in the repository.
