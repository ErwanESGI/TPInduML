import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from kedro.config import ConfigLoader
from sklearn.model_selection import train_test_split
import yaml


def preprocess_data(input_datas: pd.DataFrame) -> pd.DataFrame:
    # Supprimer les lignes contenant des valeurs nulles
    input_datas = input_datas.dropna()

    # Sauvegarder les valeurs Min et Max dans le fichier parameters.yml
    parameters_data = {
        "min_values_data": input_datas.min().min().item(),
        "max_values_data": input_datas.max().max().item()
    }

    # Initialiser le scaler MinMax
    scaler = MinMaxScaler()
    
    # Normaliser les données (Les colonnes non numériques sont exclues de la normalisation)
    numeric_columns = input_datas.select_dtypes(include=[float, int]).columns
    if not numeric_columns.empty:
        normalized_data = pd.DataFrame(scaler.fit_transform(input_datas[numeric_columns]), columns=numeric_columns)
        input_datas[numeric_columns] = normalized_data
    
    
    with open("conf/base/parameters.yml", "w") as f:
        yaml.dump(parameters_data, f)
    print(input_datas)
    return input_datas



def split_data(input_datas: pd.DataFrame) -> pd.DataFrame:
    #Récupération de 20% des données pour le test du modèle
    dfx = input_datas.loc[:,['before_exam_125_Hz','before_exam_250_Hz','before_exam_500_Hz','before_exam_1000_Hz','before_exam_2000_Hz','before_exam_4000_Hz','before_exam_8000_Hz']]
    dfy = input_datas.loc[:,['after_exam_125_Hz','after_exam_250_Hz','after_exam_500_Hz','after_exam_1000_Hz','after_exam_2000_Hz','after_exam_4000_Hz','after_exam_8000_Hz']]
    train_df_x, test_df_x, train_df_y, test_df_y = train_test_split(dfx, dfy, test_size=0.2)

    print("*********VARIABLE TRAIN*********")
    print(train_df_x, train_df_y, test_df_x, test_df_y )
    return train_df_x, train_df_y, test_df_x, test_df_y 