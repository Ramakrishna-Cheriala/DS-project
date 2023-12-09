from ChickenDiseaseClassification import logger
from src.ChickenDiseaseClassification.pipeline.stage_01_data_ingestion import (
    DataIngestionTraningPipeline,
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
