import os 
import zipfile
import gdown
from classifier import logger
from classifier.utils.utils import get_size
from classifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self)-> str:
        """
            Fetches data from the url. (from google drive in our case)
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            # NOTE:the url looks like this: https://drive.google.com/file/d/1LSY3H5Snqb7w6q1s1klrms3ZlBc3lHkl/view?usp=sharing
            # if we split the url we get: ['https', '', 'drive.google.com', 'file', 'd', "1LSY3H5Snqb7w6q1s1klrms3ZlBc3lHkl" "view?usp=sharing"]
            # the [-2] index of the split list is the file id, we attach that file if to the below prefix url and fetch data 

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id, zip_download_dir)    # downloads the dataset to the "zip_download_dir"

            logger.info(f"Dataset successfully downloaded.")

        except Exception as e:
            raise e
    
    def extract_zip_file(self):
        """
            extracts the dataset from the downloaded zip file.
        """
        unzip_path = self.config.unzip_dir
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
