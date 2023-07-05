import pytest
from kedro_galactics.pipelines.Analyse.nodes import preprocess_data
import pandas as pd
from pandas.testing import assert_frame_equal

def test_node():

    # Préparer les données d'entrée et de sortie pour le test
    input_data = pd.DataFrame({
    'before_exam_125_Hz': [1, 24, 46],
    'before_exam_250_Hz': [1, 7, 102],
    'before_exam_500_Hz': [1, None, 26],
    'before_exam_1000_Hz': [1, 109, None],
    'before_exam_2000_Hz': [1, None, 94],
    'before_exam_4000_Hz': [1, None, 116],
    'before_exam_8000_Hz': [1, None, 48],
    'after_exam_125_Hz': [1, 20, None],
    'after_exam_250_Hz': [1, 2, None],
    'after_exam_500_Hz': [1, 91, None],
    'after_exam_1000_Hz': [1, 81, None],
    'after_exam_2000_Hz': [1, None, 83],
    'after_exam_4000_Hz': [1, 50, None],
    'after_exam_8000_Hz': [1, 18, None]
    })
    expected_output = pd.DataFrame({
    'before_exam_125_Hz': [0],
    'before_exam_250_Hz': [0],
    'before_exam_500_Hz': [0],
    'before_exam_1000_Hz': [0],
    'before_exam_2000_Hz': [0],
    'before_exam_4000_Hz': [0],
    'before_exam_8000_Hz': [0],
    'after_exam_125_Hz': [0],
    'after_exam_250_Hz': [0],
    'after_exam_500_Hz': [0],
    'after_exam_1000_Hz': [0],
    'after_exam_2000_Hz': [0],
    'after_exam_4000_Hz': [0],
    'after_exam_8000_Hz': [0]
    })
    
    # Appeler le nœud à tester
    actual_output = preprocess_data(input_data) 
    print("***********ACTUEL*************")
    print(actual_output)
    print("***********Expected*************")
    print(expected_output)
    # Vérifier si le résultat obtenu correspond au résultat attendu
    assert_frame_equal(actual_output.astype(int), expected_output.astype(int))

#On test si il normalise norlamement et si il supprime bien la ligne où il y a des valeurs nulls 


#On peut rajouter un test sur si on print bien dans le parameters.yml
#Rajouter le test sur les variables d'entrainements(s'avoir si elles sont pas égale à 0 ni vide )
