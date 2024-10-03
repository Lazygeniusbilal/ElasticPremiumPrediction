import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.MLProject.exception.exception import CustomException
from src.MLProject.logger.logger import logging
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib

@dataclass
class DataTransformationConfig:
    preprocessor_object_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def data_transformation_pipeline(self):
        # Selecting the numerical and categorical columns
        logging.info("Separating the numerical and categorial columns")

        # Numerical and categorical pipeline construction
        logging.info("Initializing the pipeline construction!")
        num_pipeline = Pipeline(
            steps=[("scaler", StandardScaler())]
        )
        cat_pipeline = Pipeline(
            steps=[("Encoder", OneHotEncoder())]
        )

        logging.info("Pipeline Construction is done!")

        # Merging the numerical and categorical pipelines
        preprocessor = ColumnTransformer([
            ("num_pipeline", num_pipeline, make_column_selector(dtype_include=np.number)),
            ("cat_pipeline", cat_pipeline, make_column_selector(dtype_include=object))
        ])

        # Create the directory to save the preprocessor object
        os.makedirs(os.path.dirname(self.data_transformation_config.preprocessor_object_file_path), exist_ok=True)

        # Saving the preprocessor object
        joblib.dump(preprocessor, self.data_transformation_config.preprocessor_object_file_path)
        logging.info(f"Preprocessor object saved at {self.data_transformation_config.preprocessor_object_file_path}")

        return preprocessor

    def data_transformation(self, train_data_path, test_data_path):
        logging.info("Reading the training and testing datasets!")

        # Load the datasets
        train_data = pd.read_csv(train_data_path)
        test_data = pd.read_csv(test_data_path)

        logging.info("Splitting the features and target columns of both train and test!")
        target_column = "Premium Price"

        # Splitting train and test into features and target
        train_data_features = train_data.drop(columns=target_column, axis=1)
        train_data_target = train_data[target_column]

        test_data_features = test_data.drop(target_column, axis=1)
        test_data_target = test_data[target_column]

        logging.info("Initializing the preprocessor!")

        # Initialize the preprocessor
        preprocessor_obj = self.data_transformation_pipeline()

        logging.info("Applying the preprocessor on both dataset features!")

        # Transform the datasets
        train_data_array = preprocessor_obj.fit_transform(train_data_features)
        test_data_array = preprocessor_obj.transform(test_data_features)

        logging.info("Removing the existing columns from the dataset which are transformed!")
        # Remove the original columns (already transformed)
        train_data = train_data.drop(columns=train_data_features.columns, axis=1)
        test_data = test_data.drop(columns=test_data_features.columns, axis=1)

        # Convert the transformed data from array to dataframe
        logging.info("Converting the transformed array into dataframe!")
        train_data_transformed = pd.DataFrame(train_data_array, columns=preprocessor_obj.get_feature_names_out())
        test_data_transformed = pd.DataFrame(test_data_array, columns=preprocessor_obj.get_feature_names_out())

        return train_data_transformed, test_data_transformed, train_data_target, test_data_target

try:
    obj = DataTransformation()
    obj.data_transformation(train_data_path="artifacts/train_data.csv", test_data_path="artifacts/test_data.csv")

except Exception as e:
    raise CustomException(str(e), sys.exc_info())
