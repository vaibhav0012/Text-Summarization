import os
import sys
from transformers import AutoTokenizer
from src.Text_Summarization.logging import logger
from src.Text_Summarization.exception import CustomException
from src.Text_Summarization.config.configuration import DataTransformationConfig
from src.Text_Summarization.constants import *
from datasets import load_dataset, load_from_disk

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_example_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        dataset_samsun = load_from_disk(os.path.join(BASE_DIR,self.config.data_path))
        dataset_samsun_pt = dataset_samsun.map(self.convert_example_to_features, batched = True)
        dataset_samsun_pt.save_to_disk(os.path.join(BASE_DIR,self.config.root_dir,"samsum_dataset"))