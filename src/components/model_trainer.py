import os
import sys
from dataclasses import dataclass

from catboost import CatBoosRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,

)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerconfig:
    train_model_file_path = os.path.join("artifcats", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerconfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            models = {
                "RandomForest": RandomForestRegressor(),
                "DecisionTree": DecisionTreeRegressor(),
                "AdaBoost": AdaBoostRegressor(),
                "GradientBoost": GradientBoostingRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Redgressor": CatBoosRegressor( Verbose=False),
                "LinearRegression": LinearRegression()
            }

            params = {
                "Decision Tree": {
                    'criterion' : ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                },

                "Random Forest": {
                    'n_estimators': [10, 50, 100, 200, 300],
                },

                "Gradient Boosting":{
                    'learning_rate': [.1,.01, 0.5, .001],
                    'subsample':[0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                    'n_estimators': [8, 16, 32, 64, 128, 256],
                },

                "Linear Regression": {},

                "AdaBoost": {
                    'n_estimators': [.1, .01, 0.5, .001],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },

                "XGBRessor": {
                    'learning_rate': [.1, .01, .05, .001],
                    'n_estimators': [8, 16, 32, 64, 128, 256],
                }, 

                "CatBoost":{
                    'depth': [6, 8, 10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100],
                },
                
            }


            model_report:dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models, params=params)

            best_model_score = max(sorted(model_report.values())) # get the best model based on the score

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("Model score is less than 0.6", sys)
            
            logging.info(f"best model is {best_model_name} with score {best_model_score}")

            save_object(
                file_path=self.model_trainer_config.train_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_score = r2_score(y_test, predicted)
            return r2_score
        
        except Exception as e:
            raise CustomException(e, sys)