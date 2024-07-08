import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

def load_model():
    model = MobileNetV2(weights='imagenet')
    return model

def classify_image(model, img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    predictions = model.predict(img_array)
    return decode_predictions(predictions, top=3)[0]

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python mobilenet_image_classification.py <image_path>")
    else:
        img_path = sys.argv[1]
        model = load_model()
        result = classify_image(model, img_path)
        for pred in result:
            print(f"Predicted: {pred[1]} with probability {pred[2]:.4f}")
