import pandas as pd
import numpy as np
import csv
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_absolute_error, accuracy_score, confusion_matrix,classification_report
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, RandomTreesEmbedding
from sklearn.preprocessing import StandardScaler , LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split,KFold, cross_val_score, RandomizedSearchCV
from scipy.stats import randint, uniform 
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from ucimlrepo import fetch_ucirepo 
from sklearn.linear_model import LogisticRegression
import sqlite3
from src.modeling import data_splitting


def preprocessing():
    X_train, X_test, y_train, y_test, num_cols, cat_cols=data_splitting.data_split()

    preprocessor=ColumnTransformer(
        [
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_cols)
        ]
    )

    Pipelines=Pipeline([
        ('pre', preprocessor),
        ('model',RandomForestClassifier(random_state=42, class_weight= 'balanced'))
    ])

    return Pipelines, X_train, X_test, y_train, y_test



print(preprocessing())