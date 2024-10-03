import mlflow
import mlflow.sklearn
import os
import sys
import joblib
from src.MLProject.logger.logger import logging
from src.MLProject.exception.exception import CustomException
from src.MLProject.components.data_transformation import DataTransformation
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


class ModelEvaluation:
    
    def __init__(self):
        # Load the model
        model_path = os.path.join("artifacts", "model.pkl")
        self.model = joblib.load(model_path)
        
    def evaluation_metrics(self, true, pred):
        r2 = r2_score(true, pred)
        mae = mean_absolute_error(true, pred)
        mse = mean_squared_error(true, pred)
        return r2, mae, mse

    def model_evaluation(self, x_test, y_test):
        # Make predictions on the test data
        logging.info("Making predictions on the test data!")
        predictions = self.model.predict(x_test)

        # Calculate metrics
        logging.info("Calculating the metrics")
        r2, mae, mse = self.evaluation_metrics(y_test, predictions)

        # Log model and metrics using mlflow
        with mlflow.start_run():
            mlflow.log_param("model_name", "LGBMRegressor")
            mlflow.log_metric("r2_score", r2)
            mlflow.log_metric("mean_absolute_error", mae)
            mlflow.log_metric("mean_squared_error", mse)

try:
    data_transformation = DataTransformation()
    x_train, x_test, y_train, y_test = data_transformation.data_transformation(
        train_data_path="artifacts/train_data.csv", 
        test_data_path="artifacts/test_data.csv"
    )
    
    # Load and evaluate the model
    obj = ModelEvaluation()
    obj.model_evaluation(x_test=x_test, y_test=y_test)

except Exception as e:
    raise CustomException(str(e), sys)
