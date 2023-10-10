from fastapi import FastAPI
from starlette.responses import JSONResponse
from joblib import load
from datetime import datetime, timedelta
import pandas as pd


app = FastAPI()

# SARI_model = load('../models/SARIMAX.joblib')

# FOODS_1_df_dt_pipeline = load('../models/FOODS_1_df_dt_pipeline.joblib')
# FOODS_2_df_dt_pipeline = load('../models/FOODS_2_df_dt_pipeline.joblib')
# FOODS_3_df_dt_pipeline = load('../models/FOODS_3_df_dt_pipeline.joblib')
# HOBBIES_1_df_dt_pipeline = load('../models/HOBBIES_1_df_dt_pipeline.joblib')
# HOBBIES_2_df_dt_pipeline = load('../models/HOBBIES_2_df_dt_pipeline.joblib')
# HOUSEHOLD_1_df_dt_pipeline = load('../models/HOUSEHOLD_1_df_dt_pipeline.joblib')
# HOUSEHOLD_2_df_dt_pipeline = load('../models/HOUSEHOLD_2_df_dt_pipeline.joblib')

project_obs= "The assigned objective is to develop two distinct models that will be implemented as APIs in a production environment. This study proposes the development of a prediction model utilising a Machine Learning algorithm to effectively forecast the sales income of a particular item within a designated retailer on a specific day. This study proposes the use of a time-series analysis method to develop a forecasting model for predicting the aggregate sales income of all stores and items throughout the forthcoming seven-day period."

@app.get("/")
def read_root():
    return {"project objective": project_obs,
            "endpoints":["/","/health","/sales/national/","/sales/stores/items/"],
              "input parameters for predicting revenue of an item in a store for a specific date":["date","item_id","store_id"],
              "output format for prdictive model":"Returning predicted sales revenue",
              "input parameters for forecasting the total revenues for a spevific date":"date in str format of year-month-day",
              "output format for forecasting model":"Returning next 7 days sales revenues",
              "Github links for project ": "https://github.com/KenUTS/adv_mla_assignment_2",
              "Github links for API ": "https://github.com/KenUTS/alma_api"
            }

@app.get('/health', status_code=200)
def healthcheck():
    return 'Welcome!'

# @app.get("/sales/national/")
# def forecasting(
#     date: str
#     ):
#     date_input = datetime.strptime(date, "%Y-%m-%d")
#     date_seven=(date_input + timedelta(days=7)).strftime('%Y-%m-%d')
#     date_one=(date_input + timedelta(days=1)).strftime('%Y-%m-%d')
#     sobs = SARI_model.get_prediction(start=date_one, end=date_seven).predicted_mean
#     range = pd.date_range(start=date_one, end=date_seven).to_list()
#     date_ranges = [str(d.strftime('%Y-%m-%d')) for d in range]
#     forecast_list = {date: value for date, value in zip(date_ranges, sobs)}
#     return JSONResponse(forecast_list)

# def format_features_predictive(
#     date: str,
#     item_id: str,
#     store_id: str,
#     is_event: int
#     ):
#     return {
#         'date': [date],
#         'item_id': [item_id],
#         'store_id': [store_id],
#         'is_event': [is_event]
#     }

# def predictive_model(item_id):
#     if 'FOODS_1' in item_id:
#         return FOODS_1_df_dt_pipeline
#     elif 'FOODS_2' in item_id:
#         return FOODS_2_df_dt_pipeline
#     elif 'FOODS_3' in item_id:
#         return FOODS_3_df_dt_pipeline
#     elif 'HOBBIES_1' in item_id:
#         return HOBBIES_1_df_dt_pipeline
#     elif 'HOBBIES_2' in item_id:
#         return HOBBIES_2_df_dt_pipeline
#     elif 'HOUSEHOLD_1' in item_id:
#         return HOUSEHOLD_1_df_dt_pipeline
#     elif 'HOUSEHOLD_2' in item_id:
#         return HOUSEHOLD_2_df_dt_pipeline

# @app.get("/sales/stores/items/")
# def predict(
#     date: str,
#     item_id: str,
#     store_id: str,
#     is_event: int =0
#     ):
#     features = format_features_predictive(
#         date,
#         item_id,
#         store_id,
#         is_event
#         )
#     obs = pd.DataFrame(features)
#     obs['date'] = pd.to_datetime(obs['date'])
#     obs['day_of_month'] = obs['date'].dt.day
#     obs['month_of_year'] = obs['date'].dt.month
#     obs['day_of_week'] = obs['date'].dt.dayofweek
#     pred = predictive_model(item_id).predict(obs.drop(columns=['date']))
#     return JSONResponse(pred.tolist())