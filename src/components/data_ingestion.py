import os
import sys

from src.exception import CustomException   
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_tranformation import DataTranformationConfig
from src.components.data_tranformation import DataTranformation

#from src.components.model_trainer import ModelTrainerConfig
#from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig: #DataIngestionConfig class is responsible for storing the path of the train and test data file and raw data file.
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion: #DataIngestion class is responsible for reading the data and splitting the data into train and test set and saving the data in the artifacts folder in the form of csv file and returning the path of the train and test data file to the main function to initiate the data transformation process. 
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        def __init__(self):
            self.data_tranformation_config = DataTranformationConfig()

        def initiate_data_ingestion(self):
             logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Data has been read successfully")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train Test Split has initated successfully")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Imgestion of the Data has been completed successfully")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()

        data_transformation = DataTranformation()
        train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)

        #modeltrainer = ModelTrainer()
        #print(modeltrainer.initiate_model_trainer(train_arr, test_arr))