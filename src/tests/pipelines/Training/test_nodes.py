"""
This is a boilerplate test file for pipeline 'SelectionAndTraining'
generated using Kedro 0.18.10.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""
from sklearn.metrics import accuracy_score
import pytest
from kedro_galactics.pipelines.Training.nodes import training_model


@pytest.fixture
def model():
    return training_model('train_data', 'train_labels', 'test_data', 'test_label')

def test_model_performance(model,train_data,test_label):

    # Obtenir une instance du modèle entraîné   
    trained_model  = model()
    
    # Prédiction sur les données de test
    y_pred = trained_model.predict(train_data)

    # Calcul de la métrique de performance (ex: accuracy)
    accuracy = accuracy_score(train_data, y_pred)

    print(accuracy)
    # Vérification de la métrique de performance à l'aide d'une assertion
    assert int(accuracy) > 0.4 