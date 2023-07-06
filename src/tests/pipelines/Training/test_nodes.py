import pytest
import pandas as pd
import mlflow
from sklearn.metrics import mean_squared_error
from math import sqrt

def test_model():
    test_df_x = pd.read_csv("data/05_model_input/test.csv")
    test_df_y = pd.read_csv("data/05_model_input/test_labels.csv")

    test_df_x = test_df_x.to_numpy()
    test_df_y = test_df_y.to_numpy()
    # assert test_x.shape == test_y.shape
    test_df_x = test_df_x.reshape((-1, 7, 1))
    test_df_y = test_df_y.reshape((-1, 7, 1))
    # Vérification de l'accuracy

    # Chargement d'un modèle depuis MLflow
    model = mlflow.tensorflow.load_model('runs:/238f96bf4c96412e962aa6fe76e673d0/model')
    predictions = model.predict(test_df_x)

    test_df_y = test_df_x.reshape(-1,7)

    # Calcul du %erreurs root-mean-square
    mse = sqrt(mean_squared_error(predictions, test_df_y))
    print(mse)

pytest.main()


"""def test_model_performance(model, test_data, test_label):
    # Création du modèle
    model = create_model()
    # Prédiction sur les données de test
    y_pred = model.predict(test_data)

    # Calcul de la métrique de performance (ex: accuracy)
    accuracy = accuracy_score(test_label, y_pred)

    # Vérification de la métrique de performance à l'aide d'une assertion
    assert accuracy > 0.4  # Exemple d'assertion sur l'accuracy"""