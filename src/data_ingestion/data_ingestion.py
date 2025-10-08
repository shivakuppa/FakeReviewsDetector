import os
import sys
import subprocess
import pandas as pd
from typing import List
from pathlib import Path
import kaggle

from src.utils.logger import logger
from src.utils.exceptions import CustomException

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class DataIngestion:
    def __init__(self, kaggle_dataset: str, categories: List[str]):
        self.kaggle_dataset = kaggle_dataset
        self.categories = categories
    
    def ingest_category_from_kaggle(self, category: str):
        try:
            logger.info(f"Starting ingestion for category: {category} from Kaggle")

            dataset = self.kaggle_dataset
            file_name = f"amazon_reviews_us_{category}_v1_00.tsv"
            download_dir = os.path.join(ROOT_DIR, "data", "raw") 
            os.makedirs(download_dir, exist_ok=True)
            
            file_path = os.path.join(download_dir, file_name)
            if os.path.exists(file_path):
                logger.info(f"{category} raw file already exists")
                return
                        
            kaggle.api.authenticate()
            kaggle.api.dataset_download_files(
                dataset=dataset,
                file_name=file_name,
                path=download_dir,
                unzip=True
            )
            
            logger.info(f"Successfully ingested category: {category} from Kaggle into raw file.")

        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed: {e}", exc_info=True)
            raise CustomException(f"Kaggle download failed for category: {category}", sys)

        except Exception as e:
            logger.error(f"Error during ingestion of category ({category}) from Kaggle: {e}", exc_info=True)
            raise CustomException(e, sys)
    
    def ingest_from_kaggle(self):
        try:
            logger.info(f"Starting ingestion from Kaggle dataset: {self.kaggle_dataset}")
            for category in self.categories:
                self.ingest_category_from_kaggle(category)
            logger.info("Successfully ingested all categories from Kaggle.")
        
        except Exception as e:
            logger.error(f"Error during Kaggle ingestion: {e}", exc_info=True)
            raise CustomException(e, sys)
    
    def initiate_ingestion(self):
        try:
            logger.info("Starting data ingestion process...")
            self.ingest_from_kaggle()

        except Exception as e:
            logger.error(f"Error during data ingestion: {e}", exc_info=True)
            raise CustomException(e, sys)
