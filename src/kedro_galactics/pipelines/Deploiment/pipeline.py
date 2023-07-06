"""
This is a boilerplate pipeline 'Deploiment'
generated using Kedro 0.18.10
"""

from kedro.pipeline import node, Pipeline
from .nodes import predict

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func= predict,
            inputs="",
            outputs=None,
            name="node_deploiement"
        )  
    ])
