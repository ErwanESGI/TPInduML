"""
This is a boilerplate pipeline 'Analyse'
generated using Kedro 0.18.10
"""
from kedro.pipeline import node, Pipeline
from .nodes import preprocess_data,split_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func= preprocess_data,
            inputs="raw_daily_data",
            outputs="transform_datas",
            name="node_merge_raw_daily_data"
        ),
        node(
            func= split_data,
            inputs="transform_datas",
            outputs=["train_data","train_labels","test_data","test_labels"]
        )   
        ])
