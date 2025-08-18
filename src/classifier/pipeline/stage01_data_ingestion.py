from classifier import logger
from classifier.config.configuration import ConfigManager
from classifier.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # reads the config.yaml and retuns a DataIngestionConfig dataclass object
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()  # returns a DataIngestionConfig dataclass object
        
        # creates a DataIngestion object to download data
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # downloading the dataset
        data_ingestion.download_file()      # downloads the zipfile from the url
        data_ingestion.extract_zip_file()   # unzips the downloaded dataset zipfile 