import unittest
# Patch the missing attribute before 'ensure' tries to import it
if not hasattr(unittest.TestCase, 'assertRaisesRegexp'):
    unittest.TestCase.assertRaisesRegexp = unittest.TestCase.assertRaisesRegex

from source.CNN_Disease_Classifier import logger
from source.CNN_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e