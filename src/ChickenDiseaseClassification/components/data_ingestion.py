import os
import urllib.request as request
import zipfile
from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.utils.common import get_size
from src.ChickenDiseaseClassification.entity.config_entity import DataIngestonConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestonConfig):
        self.config = config

    def dowenload_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url, filename=self.config.local_data_file
            )
            logger.info(f"{filename} dowenload with following info: \n{headers}")
        else:
            logger.info(f"file already exists")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
