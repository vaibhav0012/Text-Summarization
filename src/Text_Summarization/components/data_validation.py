import os
import sys
from src.Text_Summarization.logging import logger
from src.Text_Summarization.exception import CustomException
from src.Text_Summarization.config.configuration import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            #artifacts\data_ingestion\samsum_dataset
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                    logger.error(f"File '{file}' not found in required files list.")
                else:
                    logger.info(f"File '{file}' found in required files list.")
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status


        except Exception as e:
            raise CustomException(e,sys)