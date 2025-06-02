import os
import requests
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)

#Component-DataIngestion

class DataIngestion:
    def __init__(self , config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            response = requests.get(self.config.source_url, stream=True)
            response.raise_for_status()  # Raises HTTPError if not 200
            with open(self.config.local_data_file, "wb") as f:
                f.write(response.content)
            logger.info(f"{self.config.local_data_file} downloaded successfully!")
        else:
            logger.info("File already exists")


    def extract_zipfile(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path , exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file , 'r') as zip_ref:
            zip_ref.extractall(unzip_path)