from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

<<<<<<< HEAD

STAGE_NAME = "Data Ingestion stage"
=======
STAGE_NAME = "Data Ingestion Stage"
>>>>>>> 8abfc0bb21c937c52792a982ac046e55392b4fdf

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

<<<<<<< HEAD



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
=======
if __name__ == "__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME} started <<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e
        
>>>>>>> 8abfc0bb21c937c52792a982ac046e55392b4fdf
