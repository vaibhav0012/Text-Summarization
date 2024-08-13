import os
import sys
from src.Text_Summarization.config.configuration import ConfigurationManager
from src.Text_Summarization.components.model_evaluation import ModelEvaluation
from src.Text_Summarization.exception import CustomException

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()
        except Exception as e:
            raise CustomException(e,sys)