from transformers import pipeline

def load_model():
    model = pipeline('sentiment-analysis', model='distilbert-base-uncased')
    return model

def analyze_text(model, text):
    return model(text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python huggingface_model.py <text>")
    else:
        text = sys.argv[1]
        model = load_model()
        result = analyze_text(model, text)
        print(result)
