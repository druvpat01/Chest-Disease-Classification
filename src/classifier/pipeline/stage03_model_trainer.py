from classifier.config.configuration import ConfigManager
from classifier.components.model_trainer import Training
from classifier import logger


STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # creating an object of Confi Manager
        config = ConfigManager()
        training_config = config.get_training_config()  # fetching the training config's
        trainer = Training(config=training_config)      # creating object of training 
        trainer.get_base_model()    # fetches the updated base model
        trainer.train_valid_generator() # generates train and valid data
        trainer.train() # fits the model over the data

if __name__ == "__main__":
    try:
        logger.info(F">>>>>> STAGE {STAGE_NAME} started <<<<<<")
        
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> STAGE {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise