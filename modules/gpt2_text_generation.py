from transformers import pipeline

def load_model():
    model = pipeline('text-generation', model='gpt2')
    return model

def generate_text(model, prompt):
    return model(prompt, max_length=50)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python gpt2_text_generation.py <prompt>")
    else:
        prompt = sys.argv[1]
        model = load_model()
        result = generate_text(model, prompt)
        print(result)
