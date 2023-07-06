"""
This is a boilerplate pipeline 'Evaluation'
generated using Kedro 0.18.10
"""

import mlflow
import mlflow.keras
import pandas as pd
from kedro.io import DataCatalog
from kedro.io import MemoryDataSet
from tensorflow.keras.models import load_model

def evaluate_model(data: pd.DataFrame, model_path: str) -> float:
    # Charger le modèle
    model = load_model(model_path)

    # Évaluer le modèle sur les données de test
    predictions = model.predict(data) 