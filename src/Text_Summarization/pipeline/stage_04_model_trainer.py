import os
import sys
from src.Text_Summarization.config.configuration import ConfigrationManager
from src.Text_Summarization.components.model_trainer import ModelTrainer
from src.Text_Summarization.exception import CustomException

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigrationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise CustomException(e,sys)
