from classifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from classifier import logger 
from classifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline


# STAGE_NAME = "Data Ingestion Stage"
     
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = DataIngestionTrainingPipeline()
#     obj.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
# except Exception as e:
#     logger.exception(e)
#     raise e 


STAGE_NAME = "Prepare base model"

try:
        logger.info(f"************************************")
        logger.info(f">>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<")

        obj = PrepareBaseModelTrainingPipeline()
        obj.main()

        logger.info(f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e