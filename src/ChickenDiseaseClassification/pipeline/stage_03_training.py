from ChickenDiseaseClassification.config.configuration import ConfigurationManager
from ChickenDiseaseClassification.components.prepare_callbacks import PrepareCallback
from ChickenDiseaseClassification.components.training import Training
from ChickenDiseaseClassification import logger
import os


STAGE_NAME = "Training"
file_path = "artifacts/training/model.h5"


class ModelTrainingPipeline:
    def __inti__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list=callback_list)


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e
