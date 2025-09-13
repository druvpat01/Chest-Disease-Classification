from classifier.config.configuration import ConfigManager
from classifier.components.evaluation import Evaluation
from classifier import logger

STAGE_NAME = "Evaluation Stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")

        obj = EvaluationPipeline()
        obj.main()

        logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e