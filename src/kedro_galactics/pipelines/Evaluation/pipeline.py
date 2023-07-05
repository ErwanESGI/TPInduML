"""
This is a boilerplate pipeline 'Evaluation'
generated using Kedro 0.18.10
"""

from kedro.pipeline import node, Pipeline
from .nodes import training_model

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func= training_model,
            inputs="",
            outputs=None,
            name="node_evaluate"
        )  
    ])
