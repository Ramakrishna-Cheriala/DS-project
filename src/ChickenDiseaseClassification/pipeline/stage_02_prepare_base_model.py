from src.ChickenDiseaseClassification.config.configuration import ConfigurationManager
from src.ChickenDiseaseClassification.components.prepare_base_model import (
    PrepareBaseModel,
)
from src.ChickenDiseaseClassification import logger


class PrepareBaseModelTraningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = PrepareBaseModelTraningPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} finished")
    except Exception as e:
        logger.exception(e)
        raise e
