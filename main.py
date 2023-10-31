from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"

try:
    logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation"

try:
    logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer"

try:
    logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e