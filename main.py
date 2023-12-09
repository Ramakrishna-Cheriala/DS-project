from ChickenDiseaseClassification import logger
from src.ChickenDiseaseClassification.pipeline.stage_01_data_ingestion import (
    DataIngestionTraningPipeline,
)
from src.ChickenDiseaseClassification.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTraningPipeline,
)


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{STAGE_NAME} started")
    obj = DataIngestionTraningPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} finished")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f"{STAGE_NAME} started")
    obj1 = PrepareBaseModelTraningPipeline()
    obj1.main()
    logger.info(f"{STAGE_NAME} finished")

except Exception as e:
    logger.exception(e)
    raise e
