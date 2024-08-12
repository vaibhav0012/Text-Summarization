import os
import urllib.request as request
import zipfile
from pathlib import Path
from src.Text_Summarization.logging import logger
from src.Text_Summarization.utils.common import get_size
from src.Text_Summarization.entitiy import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
            url = self.config.source_url,
            filename = self.config.local_data_file
            )
            print(filename,headers)
            logger.info(f"{filename} downloaded with headers{headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists of size: {get_size(Path(self.config.local_data_file))}")

    
    def extract_zip_file(self):
        unizip_path = self.config.unzip_dir
        os.makedirs(unizip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unizip_path)