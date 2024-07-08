from transformers import pipeline

def load_model():
    model = pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english')
    return model

def recognize_entities(model, text):
    return model(text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python bert_ner.py <text>")
    else:
        text = sys.argv[1]
        model = load_model()
        result = recognize_entities(model, text)
        print(result)
