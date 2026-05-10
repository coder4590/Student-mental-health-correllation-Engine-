import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from src.modeling import hyperparameter_tuning
import os
from sklearn.metrics import f1_score


def fit_predict():
    best_model, best_params, best_score, x_test, y_test = hyperparameter_tuning.hyperparameter_tuning()

    y_pred = best_model.predict(x_test)

    print(f"\nBest Params: {best_params}")
    print(f"Best CV Score: {best_score:.3f}")
    print(f"   F1 Score: {f1_score(y_test, y_pred):.3f}")
    print(f"\nTest Accuracy: {accuracy_score(y_test, y_pred):.3f}")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    model_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "models")
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(best_model, os.path.join(model_dir, 'model.pkl'))



if __name__ == "__main__":
    fit_predict()