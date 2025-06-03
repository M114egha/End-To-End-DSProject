import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
from src.datascience.entity.config_entity import  DataTransformationConfig
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config


    def train_test_split(self):
        data=pd.read_csv(self.config.data_path)

        #Split the data into traina nd test
        train , test= train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir , "train.csv") , index=False)
        test.to_csv(os.path.join(self.config.root_dir , "test.csv") , index=False)

        logger.info("Splitted teh dat ainto train and test data")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)