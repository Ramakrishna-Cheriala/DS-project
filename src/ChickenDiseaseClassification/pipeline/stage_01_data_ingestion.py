from src.ChickenDiseaseClassification.config.configuration import ConfigurationManager
from src.ChickenDiseaseClassification.components.data_ingestion import DataIngestion
from src.ChickenDiseaseClassification import logger


class DataIngestionTraningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.dowenload_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = DataIngestionTraningPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} finished")
    except Exception as e:
        logger.exception(e)
        raise e
