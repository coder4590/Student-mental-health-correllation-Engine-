import pandas as pd
import numpy as np
import csv
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_absolute_error, accuracy_score, confusion_matrix,classification_report,f1_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, RandomTreesEmbedding
from sklearn.preprocessing import StandardScaler , LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split,KFold, cross_val_score, RandomizedSearchCV
from scipy.stats import randint, uniform 
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from ucimlrepo import fetch_ucirepo 
from sklearn.linear_model import LogisticRegression
import sqlite3
from src.modeling import preprocessing

def hyperparameter_tuning():
    Pipelines, x_train, x_test, y_train, y_test=preprocessing.preprocessing()

    param_grid = {
    'model__n_estimators': [100, 200, 300, 500],
    'model__max_depth': [3, 5, 7, 10, None],
    'model__min_samples_split': [2, 5, 10, 15],
    'model__min_samples_leaf': [1, 2, 4, 8],
    'model__max_features': ['sqrt', 'log2', None],
    'model__bootstrap': [True],
    'model__class_weight': ['balanced', 'balanced_subsample', None],
    'model__max_samples': [0.5, 0.7, 0.9, None],
    'model__criterion': ['gini', 'entropy'],
}
    
    search = RandomizedSearchCV(
        estimator=Pipelines,
        param_distributions=param_grid,
        n_iter=50,  # Increase if you have time
        cv=5, # using the cross validation with the 5 cross cv 
        scoring='f1',
        n_jobs=-1,
        random_state=42,
        verbose=1
    )

    search.fit(x_train,y_train)

    print("Best Parameters:", search.best_params_)
    print("Best CV Accuracy:", search.best_score_)


    return search.best_estimator_, search.best_params_, search.best_score_, x_test, y_test


print(hyperparameter_tuning())