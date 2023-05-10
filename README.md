# Prediciting Wine Quality and Building a Recommender Wine System
Data Science project on predicting wine quality and building recommender system using two datasets - **Wine Qaulity** dataset and **Wine Reviews** dataset.

## Wine Quality

Source: https://archive.ics.uci.edu/ml/datasets/wine+quality
Citation: P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

## Wine Reviews

Source: https://www.kaggle.com/datasets/zynicide/wine-reviews
The data was scraped from http://www.winemag.com/?s=&drink_type=wine during 2017.

## Folders structure

Folder `datasets` contains all the datasets needed for the project

Folder `EDA` is for the exploratory data analysis on both datasets

Folder `Wine Quality Predict` contains a notebook with ml work with the **Wine Quality** dataset. It includes multiple linear regression, different classification models and their evaluation, pre-processing of data and its transformation, and fine-tuning hyperparametersof the best performing models.

Folder `Wine Reviews Predict and Recommend` contains work on predictive models for the **Wine Reviews** dataset as well as building recommender system

Folder `catboost_info` contains information on gradient boosting framework used in the project

Folder `web_app` contains code nesseccary to run **flask** application for our recommender system ui representation

