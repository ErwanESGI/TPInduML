import numpy as np
from unittest.mock import patch
from kedro_galactics.pipelines.Training.nodes import create_model

@patch('Training.create_model')
@patch('Training.mlflow.autolog')
def test_training_model(mock_autolog, mock_create_model):
    # Données de test fictives
    train_data = np.random.rand(100, 7, 1)
    train_labels = np.random.rand(100, 7)
    test_data = np.random.rand(20, 7, 1)
    test_labels = np.random.rand(20, 7)

    # Mocking de la fonction create_model
    mock_model = mock_create_model.return_value

    # Appel de la fonction à tester
    result = create_model(train_data, train_labels, test_data, test_labels, epochs=10, batch_size=32)

    # Vérifications
    assert result == ["train_data", "train_labels", "test_data", "test_labels"]  # Vérifie que la sortie est correcte
    mock_autolog.assert_called_once()  # Vérifie que la fonction mlflow.autolog a été appelée une fois
    mock_create_model.assert_called_once()  # Vérifie que la fonction create_model a été appelée une fois
    mock_model.fit.assert_called_once_with(train_data, train_labels, epochs=5, batch_size=32)  # Vérifie que la méthode fit a été appelée avec les bons argument