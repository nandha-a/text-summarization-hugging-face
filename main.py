from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = " Data Ingestion"

try:
    logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e