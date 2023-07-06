#pipeline_registry.py
"""Project pipelines."""

from typing import Dict
# from kedro.framework.project import find_pipelines

from kedro.pipeline import Pipeline
from kedro_galactics.pipelines import (
    Deploiment as my_pip,
) 

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.
    Returns:
    A mapping from pipeline names to ``Pipeline`` objects.
    """
    my_pipeline = my_pip.create_pipeline()
    # Return statement indicates the default sequence of modular pipelines to run
    return {
        "my_pip": my_pipeline ,
        "__default__": my_pipeline
    }

