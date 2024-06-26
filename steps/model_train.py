import logging
import pandas as pd
from zenml import step
from zenml.client import Client

from src.model_dev import LinearRegressionModel
from sklearn.base import RegressorMixin
from .config import ModelNameConfig

import mlflow

experiment_tracker = Client().active_stack.experiment_tracker

# RegressorMixin -> it will return a regressor model(can be any model)

@step(experiment_tracker=experiment_tracker.name)
def train_model(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,
    config: ModelNameConfig
) -> RegressorMixin:
    
    model = None 

    try:
        if config.model_name == "LinearRegression":
            mlflow.sklearn.autolog()
            model = LinearRegressionModel()
            trained_model = model.train(X_train, y_train)
            return trained_model
        else:
            return ValueError(f'Model {config.model_name} not supported')
    except Exception as e:
            logging.error(f'Error in training model: {e}')
            raise e
