import os
from pathlib import Path
from classifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from classifier.utils.utils import read_yaml, create_directories
from classifier.entity.config_entity import (DataIngestionConfig, 
                                             PrepareBaseModelConfig, 
                                             TrainingConfig)


class ConfigManager():
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # creating the artifacts dir to store data
        create_directories([self.config.artifacts_root])    

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config.data_ingestion

        # creating the data_ingestion folder in artifacts to store the data
        create_directories([Path(config.root_dir)])

        # creating object of DataIngestionConfig data class including our config informations
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        ) 
        return data_ingestion_config
    
    def get_prepare_base_model_config(self)-> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        # creates the prepare_base_model folder in the artifacts folder
        create_directories([Path(config.root_dir)])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_classes=self.params.CLASSES,
            params_include_top=self.params.INCLUDE_TOP,
            params_learning_rate=self.params.LEARNING_RATE,
            params_weights=self.params.WEIGHTS,
        )

        return prepare_base_model_config
    
    def get_training_config(self):
        training = self.config.training
        prepare_base_config = self.config.prepare_base_model

        # path to training data
        training_data_path = os.path.join(self.config.data_ingestion.unzip_dir, 'Chest-CT-Scan-data')

        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_config.updated_base_model_path),
            training_data=Path(training_data_path),
            params_epochs=self.params.EPOCHS,
            params_batch_size=self.params.BATCH_SIZE,
            params_image_size=self.params.IMAGE_SIZE,
            params_is_augmentation=self.params.AUGMENTATION
        )

        return training_config