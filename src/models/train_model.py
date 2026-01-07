"""
Model training script for churn prediction.

TODO: Implement model training pipeline.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# TODO: Import necessary model classes and metrics


def load_data():
    """
    Load processed feature data.
    
    TODO: Load the processed customer features CSV.
    """
    pass


def prepare_features(df):
    """
    Prepare features for modeling.
    
    TODO: 
    - Select feature columns (exclude target and IDs)
    - Handle categorical variables (one-hot encoding, etc.)
    - Return X (features) and y (target)
    """
    pass


def train_model(X_train, y_train):
    """
    Train the churn prediction model.
    
    TODO: 
    - Choose appropriate model (RandomForest, XGBoost, etc.)
    - Train the model
    - Return trained model
    """
    pass


def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance.
    
    TODO:
    - Make predictions
    - Calculate metrics (accuracy, precision, recall, F1, ROC-AUC)
    - Print classification report and confusion matrix
    """
    pass


def save_model(model, filename="churn_model.pkl"):
    """
    Save trained model.
    
    TODO: Save model using joblib or pickle.
    """
    pass


if __name__ == "__main__":
    # TODO: Implement the training pipeline
    # 1. Load data
    # 2. Prepare features
    # 3. Split data
    # 4. Train model
    # 5. Evaluate model
    # 6. Save model
    pass
