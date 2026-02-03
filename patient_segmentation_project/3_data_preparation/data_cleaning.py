"""
Data Cleaning Script
Phase 3: Data Preparation

This script performs data cleaning operations on the patient segmentation dataset.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DataCleaner:
    """Class to handle data cleaning operations."""
    
    def __init__(self, input_path, output_path):
        """
        Initialize DataCleaner.
        
        Args:
            input_path (str): Path to raw data file
            output_path (str): Path to save cleaned data
        """
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.df = None
        self.cleaning_report = []
        
    def load_data(self):
        """Load the raw data."""
        logger.info(f"Loading data from {self.input_path}")
        self.df = pd.read_csv(self.input_path)
        logger.info(f"Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        self.cleaning_report.append(f"Initial shape: {self.df.shape}")
        
    def check_duplicates(self):
        """Identify and remove duplicate rows."""
        initial_count = len(self.df)
        duplicates = self.df.duplicated().sum()
        
        if duplicates > 0:
            logger.warning(f"Found {duplicates} duplicate rows")
            self.df = self.df.drop_duplicates()
            logger.info(f"Removed {duplicates} duplicate rows")
            self.cleaning_report.append(f"Duplicates removed: {duplicates}")
        else:
            logger.info("No duplicate rows found")
            self.cleaning_report.append("No duplicates found")
    
    def handle_missing_values(self, strategy='analyze'):
        """
        Handle missing values in the dataset.
        
        Args:
            strategy (str): Strategy for handling missing values
                          'analyze' - only report missing values
                          'drop' - drop rows with missing values
                          'impute' - impute missing values
        """
        missing = self.df.isnull().sum()
        missing_pct = (missing / len(self.df)) * 100
        
        if missing.sum() > 0:
            logger.info("Missing values found:")
            for col, count in missing[missing > 0].items():
                logger.info(f"  {col}: {count} ({missing_pct[col]:.2f}%)")
                self.cleaning_report.append(f"Missing in {col}: {count} ({missing_pct[col]:.2f}%)")
            
            if strategy == 'drop':
                initial_count = len(self.df)
                self.df = self.df.dropna()
                dropped = initial_count - len(self.df)
                logger.info(f"Dropped {dropped} rows with missing values")
                self.cleaning_report.append(f"Rows dropped (missing values): {dropped}")
            
            elif strategy == 'impute':
                # Impute numerical columns with median
                num_cols = self.df.select_dtypes(include=[np.number]).columns
                for col in num_cols:
                    if self.df[col].isnull().any():
                        median_val = self.df[col].median()
                        self.df[col].fillna(median_val, inplace=True)
                        logger.info(f"Imputed {col} with median: {median_val}")
                
                # Impute categorical columns with mode
                cat_cols = self.df.select_dtypes(include=['object']).columns
                for col in cat_cols:
                    if self.df[col].isnull().any():
                        mode_val = self.df[col].mode()[0]
                        self.df[col].fillna(mode_val, inplace=True)
                        logger.info(f"Imputed {col} with mode: {mode_val}")
                
                self.cleaning_report.append("Missing values imputed")
        else:
            logger.info("No missing values found")
            self.cleaning_report.append("No missing values")
    
    def detect_outliers(self, method='iqr'):
        """
        Detect outliers in numerical columns.
        
        Args:
            method (str): Method for outlier detection ('iqr' or 'zscore')
        """
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        
        logger.info(f"Detecting outliers using {method} method")
        
        for col in num_cols:
            if method == 'iqr':
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                outliers = ((self.df[col] < lower_bound) | (self.df[col] > upper_bound)).sum()
                
            elif method == 'zscore':
                z_scores = np.abs((self.df[col] - self.df[col].mean()) / self.df[col].std())
                outliers = (z_scores > 3).sum()
            
            if outliers > 0:
                pct = (outliers / len(self.df)) * 100
                logger.info(f"  {col}: {outliers} outliers ({pct:.2f}%)")
                self.cleaning_report.append(f"Outliers in {col}: {outliers} ({pct:.2f}%)")
    
    def standardize_column_names(self):
        """Standardize column names (lowercase, underscores)."""
        original_cols = self.df.columns.tolist()
        self.df.columns = self.df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')
        new_cols = self.df.columns.tolist()
        
        if original_cols != new_cols:
            logger.info("Column names standardized")
            self.cleaning_report.append("Column names standardized")
    
    def save_cleaned_data(self):
        """Save the cleaned dataset."""
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(self.output_path, index=False)
        logger.info(f"Cleaned data saved to {self.output_path}")
        logger.info(f"Final shape: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        self.cleaning_report.append(f"Final shape: {self.df.shape}")
    
    def generate_report(self):
        """Generate a cleaning report."""
        report_path = self.output_path.parent / 'cleaning_report.txt'
        
        with open(report_path, 'w') as f:
            f.write("Data Cleaning Report\n")
            f.write("=" * 50 + "\n\n")
            for item in self.cleaning_report:
                f.write(f"{item}\n")
        
        logger.info(f"Cleaning report saved to {report_path}")
        
    def clean(self, missing_strategy='analyze', remove_outliers=False):
        """
        Execute the full cleaning pipeline.
        
        Args:
            missing_strategy (str): Strategy for handling missing values
            remove_outliers (bool): Whether to remove outliers
        """
        self.load_data()
        self.standardize_column_names()
        self.check_duplicates()
        self.handle_missing_values(strategy=missing_strategy)
        self.detect_outliers()
        self.save_cleaned_data()
        self.generate_report()
        
        logger.info("Data cleaning completed!")


def main():
    """Main function to run data cleaning."""
    # Define paths (update these based on actual file names)
    base_dir = Path(__file__).parent
    input_file = base_dir.parent / '2_data_acquisition' / 'raw_data' / 'patient_data.csv'
    output_file = base_dir.parent / '2_data_acquisition' / 'processed_data' / 'patient_data_cleaned.csv'
    
    # Check if input file exists
    if not input_file.exists():
        logger.error(f"Input file not found: {input_file}")
        logger.error("Please run the data acquisition script first")
        logger.error("Or update the input_file path in this script")
        return
    
    # Create cleaner and run cleaning
    cleaner = DataCleaner(input_file, output_file)
    cleaner.clean(missing_strategy='impute', remove_outliers=False)


if __name__ == '__main__':
    main()
