import os
import sys
from src.Text_Summarization.config.configuration import ConfigrationManager
from src.Text_Summarization.components.data_validation import DataValidation
from src.Text_Summarization.exception import CustomException

class DataValidationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigrationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise CustomException(e,sys)