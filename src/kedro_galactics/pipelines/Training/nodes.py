import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import regularizers
import mlflow
import mlflow.keras

def create_model(input_shape=(7, 1), units=256, activation='relu', l2_value=0.005, dropout_rate=0.5, learning_rate=1e-3):
    # Définition de la couche d'entrée
    inputs = layers.Input(shape=input_shape)

    # Définition des couches de convolution
    x = layers.Conv1D(filters=32, kernel_size=3, activation=activation)(inputs)
    x = layers.MaxPooling1D(pool_size=2)(x)
    x = layers.ZeroPadding1D(padding=1)(x)
    x = layers.Conv1D(filters=64, kernel_size=3, activation=activation)(x)
    x = layers.ZeroPadding1D(padding=1)(x)
    x = layers.MaxPooling1D(pool_size=2)(x)

    # Aplatir les données
    x = layers.Flatten()(x)

    # Définition des couches entièrement connectées
    x = layers.Dense(units, activation='relu', kernel_regularizer=regularizers.l2(l2_value))(x)
    if dropout_rate is not None:
        x = layers.Dropout(dropout_rate)(x)
    x = layers.Dense(input_shape[0], activation='softmax')(x)

    # Création du modèle
    model = tf.keras.Model(inputs=inputs, outputs=x)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss="mse", metrics=[tf.keras.metrics.CategoricalAccuracy()])

    return model


def training_model(train_data, train_labels, test_data, test_label, epochs=10, batch_size=64):
    # Création du modèle
    model = create_model()

    mlflow.autolog()

    # Entraînement du modèle
    model.fit(train_data, train_labels, epochs=epochs, batch_size=batch_size)




