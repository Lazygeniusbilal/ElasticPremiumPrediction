import os
import sys
import numpy as np
import pandas as pd
import joblib
from lightgbm import LGBMRegressor
from dataclasses import dataclass
from src.MLProject.logger.logger import logging
from src.MLProject.exception.exception import CustomException
from src.MLProject.components.data_transformation import DataTransformation

@dataclass
class ModelTrainerConfig:
    model_filepath = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def model_training(self, x_train: pd.DataFrame, x_test: pd.DataFrame, y_train: pd.Series, y_test: pd.Series):
        logging.info("Initializing the LGBMRegressor!")
        model = LGBMRegressor()

        logging.info("Fitting the LGBMRegressor model!")
        # Fit the model on the training data
        lgbm_model = model.fit(x_train, y_train)

        logging.info("Dumping the model into the artifacts folder!")
        # Dump the model using joblib
        joblib.dump(lgbm_model, self.model_trainer_config.model_filepath)

try:
    # Call the data transformation process
    data_transformation = DataTransformation()
    x_train, x_test, y_train, y_test = data_transformation.data_transformation(
        train_data_path="artifacts/train_data.csv", 
        test_data_path="artifacts/test_data.csv"
    )
    
    # Initialize the model trainer and train the model
    obj = ModelTrainer()
    obj.model_training(x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test)

except Exception as e:
    raise CustomException(str(e), sys)
