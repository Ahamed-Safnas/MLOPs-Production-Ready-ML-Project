import os
from datetime import date
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"

# MONGODB_URL_KEY = "MONGODB_URL"
MONGODB_URL_KEY = os.getenv("MONGODB_URL")

PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "usvisa.csv"
MODEL_FILE_NAME = "model.pkl"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"