from ChickenDiseaseClassification import logger
from src.ChickenDiseaseClassification.pipeline.stage_01_data_ingestion import (
    DataIngestionTraningPipeline,
)
from src.ChickenDiseaseClassification.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTraningPipeline,
)
from src.ChickenDiseaseClassification.pipeline.stage_03_training import (
    ModelTrainingPipeline,
)

from src.ChickenDiseaseClassification.pipeline.stage_04_evaluation import (
    EvaluationPipeline,
)

import os


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{STAGE_NAME} started\n")
    obj = DataIngestionTraningPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} finished\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f"{STAGE_NAME} started\n")
    obj1 = PrepareBaseModelTraningPipeline()
    obj1.main()
    logger.info(f"{STAGE_NAME} finished\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
file_path = r"C:\Users\ramak\OneDrive\Desktop\P2\DS_project\DS-project\artifacts\training\model.h5"
try:
    if os.path.exists(file_path):
        logger.info(f"{STAGE_NAME} model already exists\n")

    else:
        logger.info(f"{STAGE_NAME} started\n")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} stage completed\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation"


try:
    logger.info(f"{STAGE_NAME} started\n")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} stage completed\n")
except Exception as e:
    logger.exception(e)
    raise e
