import sys
import pandas as pd
from src.MLProject.components.model_evaluation import ModelEvaluation
from src.MLProject.components.data_transformation import DataTransformation
from src.MLProject.logger.logger import logging
from src.MLProject.exception.exception import CustomException


class ModelPredictionPipeline:
    
    def __init__(self) -> None:
        self.model_evaluation = ModelEvaluation()
    
    def model_prediction(self, x_test: pd.DataFrame, y_test: pd.Series):
        # prediction 
        logging.info("Evaluating the model!")
        self.model_evaluation.model_evaluation(x_test=x_test, y_test=y_test)


if __name__ == "__main__":
    try:
        # Perform data transformation
        data_transformation = DataTransformation()
        x_train, x_test, y_train, y_test = data_transformation.data_transformation(
            train_data_path="artifacts/train_data.csv", 
            test_data_path="artifacts/test_data.csv"
        )
    
        # Run model prediction
        obj = ModelPredictionPipeline()
        obj.model_prediction(x_test=x_test, y_test=y_test)
    except Exception as e:
        raise CustomException(str(e), sys)
