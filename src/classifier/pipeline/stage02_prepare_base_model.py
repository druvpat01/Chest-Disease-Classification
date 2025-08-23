from classifier.config.configuration import ConfigManager
from classifier.components.prepare_base_model import PrepareBaseModel
from classifier import logger

STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # read the config.yaml and params.yaml and returns a PrepareBaseModelConfig dataclass object
        config = ConfigManager()
        base_model_config = config.get_prepare_base_model_config() # returns a PrepareBaseModelConfig dataclass object

        # creates a Prepare Base model object to download and update the base model
        prepare_base_model = PrepareBaseModel(base_model_config)
        
        prepare_base_model.get_base_model()     # downloads the base model
        prepare_base_model.update_base_model( ) # modifies the base model 


if __name__ == '__main__':
    try:
        logger.info(f"************************************")
        logger.info(f">>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<")

        obj = PrepareBaseModelTrainingPipeline()
        obj.main()

        logger.info(f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e