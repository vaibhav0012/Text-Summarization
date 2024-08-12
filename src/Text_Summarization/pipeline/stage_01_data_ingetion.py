from src.Text_Summarization.config.configuration import ConfigrationManager
from src.Text_Summarization.components.data_ingestion import DataIngestion
from src.Text_Summarization.logging import logger
from src.Text_Summarization.exception import CustomException
import sys

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigrationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config = data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise CustomException(e,sys)