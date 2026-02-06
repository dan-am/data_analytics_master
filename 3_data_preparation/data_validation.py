"""
Data Validation Script
Phase 3: Data Preparation

This script validates the quality of the patient segmentation dataset.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DataValidator:
    """Class to validate data quality."""
    
    def __init__(self, data_path):
        """Initialize DataValidator."""
        self.data_path = Path(data_path)
        self.df = None
        self.validation_results = {}
        
    def load_data(self):
        """Load the data."""
        logger.info(f"Loading data from {self.data_path}")
        self.df = pd.read_csv(self.data_path)
        
    def validate_completeness(self):
        """Check data completeness."""
        total_cells = self.df.shape[0] * self.df.shape[1]
        missing_cells = self.df.isnull().sum().sum()
        completeness = ((total_cells - missing_cells) / total_cells) * 100
        
        self.validation_results['completeness'] = completeness
        logger.info(f"Data Completeness: {completeness:.2f}%")
        
        return completeness >= 95  # Pass if >= 95% complete
    
    def validate_uniqueness(self, id_column=None):
        """Check for duplicate records."""
        duplicates = self.df.duplicated().sum()
        self.validation_results['duplicates'] = duplicates
        
        if duplicates > 0:
            logger.warning(f"Found {duplicates} duplicate records")
            return False
        else:
            logger.info("No duplicate records found ✓")
            return True
    
    def validate_data_types(self):
        """Validate data types are consistent."""
        logger.info("Data Types:")
        for col, dtype in self.df.dtypes.items():
            logger.info(f"  {col}: {dtype}")
        
        self.validation_results['data_types'] = self.df.dtypes.to_dict()
        return True
    
    def validate_value_ranges(self, range_rules=None):
        """
        Validate that values are within expected ranges.
        
        Args:
            range_rules (dict): Dictionary of column: (min, max) rules
        """
        if range_rules is None:
            range_rules = {}
        
        violations = []
        
        for col, (min_val, max_val) in range_rules.items():
            if col in self.df.columns:
                out_of_range = ((self.df[col] < min_val) | (self.df[col] > max_val)).sum()
                if out_of_range > 0:
                    violations.append(f"{col}: {out_of_range} values out of range [{min_val}, {max_val}]")
        
        self.validation_results['range_violations'] = violations
        
        if violations:
            logger.warning("Range validation violations:")
            for v in violations:
                logger.warning(f"  {v}")
            return False
        else:
            logger.info("All values within expected ranges ✓")
            return True
    
    def generate_validation_report(self):
        """Generate a validation report."""
        report_path = self.data_path.parent / 'validation_report.txt'
        
        with open(report_path, 'w') as f:
            f.write("Data Validation Report\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Dataset: {self.data_path.name}\n")
            f.write(f"Rows: {self.df.shape[0]}\n")
            f.write(f"Columns: {self.df.shape[1]}\n\n")
            
            for key, value in self.validation_results.items():
                f.write(f"{key}: {value}\n")
        
        logger.info(f"Validation report saved to {report_path}")
    
    def validate(self, range_rules=None):
        """Run all validation checks."""
        self.load_data()
        
        results = {
            'completeness': self.validate_completeness(),
            'uniqueness': self.validate_uniqueness(),
            'data_types': self.validate_data_types(),
            'ranges': self.validate_value_ranges(range_rules)
        }
        
        self.generate_validation_report()
        
        if all(results.values()):
            logger.info("\n✓ All validation checks passed!")
            return True
        else:
            logger.warning("\n✗ Some validation checks failed")
            return False


def main():
    """Main function to run data validation."""
    base_dir = Path(__file__).parent
    data_file = base_dir.parent / '2_data_acquisition' / 'processed_data' / 'patient_data_cleaned.csv'
    
    if not data_file.exists():
        logger.error(f"Data file not found: {data_file}")
        logger.error("Please run data_cleaning.py first")
        return
    
    validator = DataValidator(data_file)
    
    # Define validation rules (customize based on your data)
    range_rules = {
        # Example: 'age': (0, 120),
        # Example: 'blood_pressure': (60, 200),
    }
    
    validator.validate(range_rules=range_rules)


if __name__ == '__main__':
    main()
