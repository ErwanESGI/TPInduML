"""
This is a boilerplate pipeline 'Analyse'
generated using Kedro 0.18.10
"""
from kedro.pipeline import node, Pipeline
from .nodes import training_model

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func= training_model,
            inputs=["train_data","train_labels","test_data","test_labels"],
            outputs=None,
            name="node_trained_data"
        )  
    ])
