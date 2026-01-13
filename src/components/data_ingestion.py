import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:

    train_data_path: str = os.path.join("Artifacts", "train.csv")
    # out put is C:\Users\MyPC\Downloads\ML_PROJECT\src\\components\\Artifacts\\train.csv'
    test_data_path: str = os.path.join("Artifacts", "test.csv")
    raw_data_path: str = os.path.join("Artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(
                "notebook\\data\\stud.csv"
            )  # we can change the path and connect to any db
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            """
            os.makedirs() creates directories only.
            Passing a file path (e.g., Artifacts/train.csv) would incorrectly create
            a folder named 'train.csv'. To avoid this, we create only the parent
            directory using os.path.dirname(file_path).
            """
            logging.info("Saving raw data in the Artifacts directory")
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header=True)
            logging.info("Saved raw data in the Artifacts directory")
            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, random_state= 42, test_size=0.2)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header=True)
            logging.info("Ingestion of data completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)



if __name__ =="__main__":
    stud = DataIngestion()
    stud.initiate_data_ingestion()