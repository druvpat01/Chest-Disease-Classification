from classifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from classifier.utils.utils import read_yaml, create_directories
from classifier.entity.config_entity import DataIngestionConfig


class ConfigManager():
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # creating the artifacts dir to store data
        create_directories([self.config.artifacts_root])    

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config.data_ingestion

        # creating the data_ingestion folder in artifacts to store the data
        create_directories([config.root_dir])

        # creating object of DataIngestionConfig data class including our config informations
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        ) 
        return data_ingestion_config