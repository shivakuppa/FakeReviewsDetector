import sys
import time
import os
import pandas as pd

from src.utils.logger import logger
from src.utils.exceptions import CustomException
from src.data_ingestion.data_ingestion import DataIngestion

def run_pipeline():
    logger.info("Starting the data pipeline...")

    try:
        logger.debug("Step 1: Extracting data from source...")
        time.sleep(1)
        logger.info("Data extraction successful.")

        logger.debug("Step 2: Transforming data...")
        # Simulate a warning
        logger.warning("Data column 'age' contains null values.")
        time.sleep(1)
        logger.info("Data transformation completed.")

        logger.debug("Step 3: Loading data into database...")
        time.sleep(1)
        raise ValueError("Database connection failed!")  # simulate error

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)

    finally:
        logger.info("Pipeline execution finished.")
        

def divide_numbers(a, b):
    try:
        return a / b
    except Exception as e:
        # Raise your custom exception
        raise CustomException(e, sys)


def main():
    try:
        logger.info("=== Starting main data ingestion test ===")

        # Example Kaggle dataset and categories
        kaggle_dataset = "cynthiarempel/amazon-us-customer-reviews-dataset"
        categories = ["Automotive", "Office_Products", "Outdoors", "Shoes", "Video_Games"]  # Use a few small categories first

        ingestion = DataIngestion(kaggle_dataset=kaggle_dataset, categories=categories)
        ingestion.initiate_ingestion()  # Make sure the function name matches!

        logger.info("=== Data ingestion completed successfully ===")

    except Exception as e:
        logger.error(f"Unexpected error in main: {e}", exc_info=True)
        raise CustomException(e, sys)

if __name__ == "__main__":
    main()