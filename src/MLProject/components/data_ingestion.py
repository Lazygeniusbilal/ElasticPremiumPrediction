import os
import sys

# Determine the root directory of your project
# Assuming this script is in src/MLProject/components
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))  
sys.path.append(project_root)  # Add the project root to the system path

# Now you can import your modules
from src.MLProject.logger.logger import logging
from src.MLProject.exception.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
import os

class DataIngestion:
    
    def __init__(self):
        self.root_directory = "artifacts"
        self.raw_data_directory = "artifacts/raw_data.csv"
        self.train_data_directory = "artifacts/train_data.csv"
        self.test_data_directory = "artifacts/test_data.csv"
    
    def data_ingestion(self):
        logging.info("Data Ingestion has Started!")
        # read the dataset from the url
        data = pd.read_csv("https://github.com/yakobodata/Athena_motor_insurance/raw/refs/heads/main/motor_insurance_dataset.csv")
        # now make a directory for it to store as raw
        os.makedirs(self.root_directory, exist_ok=True)
        # now store the data into that destination
        data.to_csv(self.raw_data_directory, index=False)
        logging.info("Data is Ingested!")
    
    def split_data_into_train_and_test(self):
        logging.info("Train, Test Split started")
        data = pd.read_csv(self.raw_data_directory)  # Read the raw data before splitting
        train_data, test_data = train_test_split(data, test_size=0.25)
        # add the data into their respective destinations
        train_data.to_csv(self.train_data_directory, index=False)
        test_data.to_csv(self.test_data_directory, index=False)
        logging.info("Train Test split is done!")

try:
    obj = DataIngestion()
    obj.data_ingestion()
    obj.split_data_into_train_and_test()

except Exception as e:
    CustomException(sys, e)