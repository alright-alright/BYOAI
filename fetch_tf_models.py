import json

def fetch_tf_models():
    # Manually defined list of TensorFlow models
    models = [
        {"name": "mobilenet_v2", "description": "MobileNetV2 model", "url": "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"},
        {"name": "inception_v3", "description": "InceptionV3 model", "url": "https://tfhub.dev/google/tf2-preview/inception_v3/classification/4"},
        {"name": "resnet_v2_50", "description": "ResNet V2 50", "url": "https://tfhub.dev/google/imagenet/resnet_v2_50/classification/5"},
        {"name": "bert_en_uncased_L-12_H-768_A-12", "description": "BERT Base, Uncased", "url": "https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/3"},
        {"name": "ssd_mobilenet_v2", "description": "SSD MobileNet V2", "url": "https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2"}
    ]
    return models

def save_tf_models(models):
    try:
        with open("tf_models.json", "w") as f:
            json.dump(models, f, indent=4)
        print("TensorFlow models have been saved to tf_models.json.")
    except Exception as e:
        print(f"Error saving TensorFlow models: {e}")

def main():
    tf_models = fetch_tf_models()
    save_tf_models(tf_models)
    for model in tf_models:
        print(f"Model --> {model['name']} | Description --> {model['description']} | URL --> {model['url']}")

if __name__ == "__main__":
    main()
