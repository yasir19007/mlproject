from source.mlproject.exception import CustomException
from source.mlproject.logger import logging
import sys
from source.mlproject.components.data_ingestion import DataIngestion, DataIngestionConfig

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception : Divisble by ZERO" )
        raise CustomException(e, sys)