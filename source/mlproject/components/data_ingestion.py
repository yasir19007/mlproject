# mySql ==> Train test split ==> dataset

import os
import sys
from source.mlproject.exception import CustomException
from source.mlproject.logger import logging
import pandas as pd
from source.mlproject.utils import read_sql_data
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts', 'train.csv')
    test_data_path:str=os.path.join('artifacts', 'test.csv')
    raw_data_path:str=os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # reading the data from database
            # df = read_sql_data()
            df = pd.read_csv(os.path.join('notebook/data', 'raw.csv'))

            logging.info("Reading data from mysql database")

            # the raw data that will come from DB will be stored, so we have to given the path
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)    

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)    
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)    

            logging.info("Data ingestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
    