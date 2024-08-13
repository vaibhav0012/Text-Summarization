from src.Text_Summarization.logging import logger
from src.Text_Summarization.pipeline.stage_01_data_ingetion import DataIngestionPipeline
from src.Text_Summarization.pipeline.stage_02_data_validation import DataValidationPipeline
from src.Text_Summarization.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.Text_Summarization.exception import CustomException
import sys

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    raise CustomException(e,sys)

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    raise CustomException(e,sys)

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    raise CustomException(e,sys)
