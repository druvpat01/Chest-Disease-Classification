from classifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from classifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from classifier.pipeline.stage03_model_trainer import ModelTrainingPipeline
from classifier.pipeline.stage04_evaluation import EvaluationPipeline
from classifier import logger 

import warnings
warnings.filterwarnings('ignore')

# Data Ingestion Pipeline
# STAGE_NAME = "Data Ingestion Stage"
     
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = DataIngestionTrainingPipeline()
#     obj.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
# except Exception as e:
#     logger.exception(e)
#     raise e 


# # Preparing the Base Model
# STAGE_NAME = "Prepare base model"

# try:
#     logger.info(f"************************************")
#     logger.info(f">>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<")

#     prepare_base_model = PrepareBaseModelTrainingPipeline()
#     prepare_base_model.main()

#     logger.info(f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<")
# except Exception as e:
#     logger.exception(e)
#     raise e



# Training the model
STAGE_NAME = "Training"

try:
    logger.info(F">>>>>> STAGE {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> STAGE {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise


# Evaluating the results
STAGE_NAME = "Evaluation Pipeline"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")

    obj = EvaluationPipeline()
    obj.main()

    logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e