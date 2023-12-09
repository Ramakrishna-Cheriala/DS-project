from src.ChickenDiseaseClassification.constants import *
from src.ChickenDiseaseClassification.utils.common import read_yaml, create_directory
from src.ChickenDiseaseClassification.entity.config_entity import (
    DataIngestonConfig,
    PrepareBaseModelConfig,
)


class ConfigurationManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ):
        print(config_filepath, "\n", params_filepath)

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directory([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestonConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        data_ingestion_config = DataIngestonConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_dir_files,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directory([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
            params_batch_size=self.params.BATCH_SIZE,
            params_epochs=self.params.EPOCHS,
        )

        return prepare_base_model_config
