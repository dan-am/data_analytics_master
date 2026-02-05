"""
Data Download Script for Patient Segmentation Project
Phase 2: Data Acquisition

This script downloads the patient segmentation dataset from Kaggle.

Prerequisites:
1. Kaggle account created
2. Kaggle API credentials configured (~/.kaggle/kaggle.json)
3. kaggle package installed (pip install kaggle)

Usage:
    python download_data.py
"""

import os
import sys
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def setup_directories():
    """Create necessary directories for data storage."""
    current_dir = Path(__file__).parent
    raw_data_dir = current_dir / 'raw_data'
    processed_data_dir = current_dir / 'processed_data'
    
    raw_data_dir.mkdir(exist_ok=True)
    processed_data_dir.mkdir(exist_ok=True)
    
    logger.info(f"Data directories created/verified:")
    logger.info(f"  - Raw data: {raw_data_dir}")
    logger.info(f"  - Processed data: {processed_data_dir}")
    
    return raw_data_dir, processed_data_dir


def check_kaggle_credentials():
    """Verify that Kaggle credentials are configured."""
    kaggle_json = Path.home() / '.kaggle' / 'kaggle.json'
    
    if not kaggle_json.exists():
        logger.error("Kaggle credentials not found!")
        logger.error("Please follow these steps:")
        logger.error("1. Go to https://www.kaggle.com/account")
        logger.error("2. Click 'Create New API Token'")
        logger.error("3. Place kaggle.json in ~/.kaggle/")
        logger.error("4. Run: chmod 600 ~/.kaggle/kaggle.json")
        return False
    
    logger.info("Kaggle credentials found ✓")
    return True


def download_dataset(raw_data_dir):
    """Download the patient segmentation dataset from Kaggle."""
    try:
        import kaggle
        
        dataset_name = 'nudratabbas/patient-segmentation-data'
        logger.info(f"Downloading dataset: {dataset_name}")
        logger.info("This may take a few minutes...")
        
        # Download dataset to raw_data directory
        kaggle.api.dataset_download_files(
            dataset_name,
            path=str(raw_data_dir),
            unzip=True
        )
        
        logger.info("Dataset downloaded successfully! ✓")
        
        # List downloaded files
        files = list(raw_data_dir.glob('*'))
        logger.info(f"\nDownloaded files ({len(files)}):")
        for file in files:
            if file.is_file():
                size_mb = file.stat().st_size / (1024 * 1024)
                logger.info(f"  - {file.name} ({size_mb:.2f} MB)")
        
        return True
        
    except ImportError:
        logger.error("Kaggle package not installed!")
        logger.error("Install it with: pip install kaggle")
        return False
    except Exception as e:
        logger.error(f"Error downloading dataset: {str(e)}")
        return False


def create_data_source_documentation(dataset_name='nudratabbas/patient-segmentation-data'):
    """Create documentation about the data source."""
    current_dir = Path(__file__).parent
    doc_dir = current_dir / 'data_sources'
    doc_dir.mkdir(exist_ok=True)
    
    doc_file = doc_dir / 'dataset_info.md'
    
    content = f"""# Patient Segmentation Dataset

## Source Information

**Dataset Name:** Patient Segmentation Data

**Source:** Kaggle

**URL:** https://www.kaggle.com/datasets/{dataset_name}

**Author:** Nudrat Abbas

**License:** Check Kaggle dataset page for license information

**Downloaded:** {Path().cwd()}

## Description

This dataset contains patient information for segmentation analysis. It is designed for healthcare analytics and patient clustering applications.

## Dataset Characteristics

- **Type:** Multivariate
- **Subject Area:** Healthcare
- **Format:** CSV
- **Use Case:** Patient Segmentation, Clustering Analysis

## Important Notes

1. This is a public dataset from Kaggle
2. Check the dataset page for the most current description and license
3. Review data privacy considerations before using in production
4. Cite the dataset appropriately in any publications

## Download Date

Dataset was downloaded on: [Timestamp will be added during download]

## File Structure

[To be updated after download with actual file names and descriptions]

## Citation

If you use this dataset, please cite:
- Dataset creator: Nudrat Abbas
- Source: Kaggle
- URL: https://www.kaggle.com/datasets/{dataset_name}

## Next Steps

After downloading:
1. Review the data files in `raw_data/` directory
2. Create a data dictionary documenting all fields
3. Perform initial data quality assessment
4. Move to Phase 3: Data Preparation
"""
    
    with open(doc_file, 'w') as f:
        f.write(content)
    
    logger.info(f"Data source documentation created: {doc_file}")


def main():
    """Main function to orchestrate data download."""
    logger.info("="*60)
    logger.info("Patient Segmentation Project - Data Download")
    logger.info("Phase 2: Data Acquisition")
    logger.info("="*60)
    
    # Step 1: Check Kaggle credentials
    if not check_kaggle_credentials():
        sys.exit(1)
    
    # Step 2: Setup directories
    raw_data_dir, processed_data_dir = setup_directories()
    
    # Step 3: Download dataset
    success = download_dataset(raw_data_dir)
    
    if not success:
        logger.error("Data download failed!")
        sys.exit(1)
    
    # Step 4: Create documentation
    create_data_source_documentation()
    
    logger.info("\n" + "="*60)
    logger.info("Data acquisition completed successfully!")
    logger.info("="*60)
    logger.info("\nNext steps:")
    logger.info("1. Review the downloaded data in raw_data/")
    logger.info("2. Create a data dictionary")
    logger.info("3. Proceed to Phase 3: Data Preparation")


if __name__ == '__main__':
    main()
