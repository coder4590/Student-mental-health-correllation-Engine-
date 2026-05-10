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
from src.analysis import data_cleaning 




def data_split():

    df=data_cleaning.clean_data()

    severe_classes = ['Severe Depression', 'Moderate Severe Depression']
    df['depression_binary'] = df['depression_phq9'].apply(
        lambda x: 1 if x in severe_classes else 0
    )

    df['chronic_illness_clean'] = df['chronic_illness'].apply(
    lambda x: 'Yes' if 'হ্যাঁ' in str(x) or 'Yes' in str(x) else 'No'
    )   


    target = 'depression_binary'
    removed_feature = ['chronic_illness','depression_phq9', target]
    
    numerical_features=df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = df.select_dtypes(include=['object','category']).columns.tolist()


    final_numerical_col=[col for col in numerical_features if col not in removed_feature]
    final_categorical_col=[col for col in categorical_features if col not in removed_feature]

    x=df[final_numerical_col + final_categorical_col]
    y=df[target]

    x_train,x_test,y_train,y_test=train_test_split(
        x,y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return x_train, x_test, y_train, y_test, final_numerical_col, final_categorical_col




print(data_split())