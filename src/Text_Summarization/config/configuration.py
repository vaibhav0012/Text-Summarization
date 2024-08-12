from src.Text_Summarization.constants import *
from src.Text_Summarization.utils.common import read_yaml, create_directories
from src.Text_Summarization.entitiy import DataIngestionConfig

class ConfigrationManager:
    def __init__(self, 
                 params_filepath= PARAMS_FILE_PATH,
                 config_filepath= CONFIG_FILE_PATH
                 ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        #print(config.root_dir)
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config