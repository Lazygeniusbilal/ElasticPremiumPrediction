import sys
import os
from src.MLProject.components.data_ingestion import DataIngestion
from src.MLProject.components.data_transformation import DataTransformation
from src.MLProject.components.model_training import ModelTrainer
from src.MLProject.logger.logger import logging
from src.MLProject.exception.exception import CustomException

class ModelTrainingPipeline:
    
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()
        
    def training_pipeline(self):
        try:
            # Data Ingestion step
            train_data_path, test_data_path = self.data_ingestion.data_ingestion()
            
            # Data Transformation step
            x_train, x_test, y_train, y_test = self.data_transformation.data_transformation(
                train_data_path, test_data_path)
            
            # Model Training step
            self.model_trainer.model_training(x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test)
            
        except Exception as e:
            logging.error(f"Error in training pipeline: {e}")
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    try:
        obj = ModelTrainingPipeline()
        obj.training_pipeline()
    except Exception as e:
        raise CustomException(str(e), sys)