import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.loggers import logging
from dataclasses import dataclass


class DataIngestion:
    def __init__(self):
        self.root_file=os.path.join("artifacts")
        self.train_file_path=self.root_file +"//"+ "train_data.csv"
        self.test_file_path=self.root_file +"//" +"test_data.csv"
        self.raw_file_path=self.root_file+"//"+"raw_data.csv"

    def initiate_train_test_split(self):
        os.makedirs(self.root_file,exist_ok=True)
        DATA_FILEPATH="src\X_train.csv"
        raw_data=pd.read_csv(DATA_FILEPATH)

        train_data,test_data=train_test_split(raw_data,test_size=0.2,random_state=42)
        train_data.to_csv(self.train_file_path,index=False)
        train_data.to_csv(self.train_file_path,index=False)
        test_data.to_csv(self.test_file_path,index=False)
        raw_data.to_csv(self.raw_file_path,index=False)

        return self.train_file_path,self.test_file_path,self.raw_file_path
        

if __name__ == "__main__":
    dataingestion=DataIngestion()
    dataingestion.initiate_train_test_split()
