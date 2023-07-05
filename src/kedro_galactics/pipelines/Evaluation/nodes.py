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
    # Calculer la précision (ou toute autre métrique souhaitée)
    accuracy = ...  # Calculer la précision en comparant les prédictions avec les étiquettes réelles

    return accuracy


def evaluate_model_node(data: pd.DataFrame, model_path: str) -> pd.DataFrame:
    # Évaluer le modèle
    accuracy = evaluate_model(data, model_path)

    # Enregistrer la précision dans MLflow
    mlflow.log_metric("accuracy", accuracy)

    # Créer un DataFrame avec les résultats
    results = pd.DataFrame({"accuracy": [accuracy]})

    return results


def create_evaluate_model_node():
    return evaluate_model_node


def register_evaluate_model_node(catalog: DataCatalog):
    # Enregistrer le nœud dans le catalogue de données
    catalog.add(
        "evaluate_model",
        MemoryDataSet(),
        create_evaluate_model_node,
        inputs={"data": "test_data", "model_path": "model_path"},
        tags=["evaluate"],
    )
