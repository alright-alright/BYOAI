import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Example training data for a simple model
train_texts = ["This is a good movie", "This is a bad movie", "I love this movie", "I hate this movie"]
train_labels = [1, 0, 1, 0]

# Tokenize and pad sequences
tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(train_texts)
train_sequences = tokenizer.texts_to_sequences(train_texts)
train_padded = pad_sequences(train_sequences, maxlen=10)

# Simple model for demonstration
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=100, output_dim=16, input_length=10),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_padded, np.array(train_labels), epochs=10)

def classify_text(model, text):
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=10)
    prediction = model.predict(padded)
    return "Positive" if prediction[0][0] > 0.5 else "Negative"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python text_classification.py <text>")
    else:
        text = sys.argv[1]
        result = classify_text(model, text)
        print(result)
