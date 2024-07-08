import tensorflow as tf
import numpy as np

def load_model():
    # For demonstration, we use a simple sequential model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    # Normally you would load an existing model:
    # model = tf.keras.models.load_model('path/to/your/model')
    return model

def predict(model, input_data):
    return model.predict(input_data)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python tensorflow_model.py <input_data>")
    else:
        input_data = np.random.random((1, 784))  # Example input data
        model = load_model()
        result = predict(model, input_data)
        print(result)
