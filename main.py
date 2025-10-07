import sys
import time
from src.utils.logger import logger
from src.utils.exceptions import CustomException

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

if __name__ == "__main__":
    logger.info("Starting test for CustomException...")

    try:
        result = divide_numbers(10, 0)  # This will trigger a ZeroDivisionError
        logger.info(f"Result: {result}")
    except CustomException as ce:
        logger.error(f"Caught CustomException: {ce}")
        print("An error occurred! Check logs/error/ for details.")
