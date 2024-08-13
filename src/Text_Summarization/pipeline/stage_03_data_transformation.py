import os
import sys
from src.Text_Summarization.config.configuration import ConfigrationManager
from src.Text_Summarization.components.data_transformation import DataTransformation
from src.Text_Summarization.exception import CustomException

class DataTransformationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigrationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise CustomException(e,sys)