import json
import re
import pandas as pd

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the model
model_path = 'RNNModel.h5'  
model = load_model(model_path)

# Normalize the input data
def normalize(data):
    normalized = []
    for i in data:
        i = str(i)  # Convert to string
        i = i.lower()  # Convert to lowercase
        i = re.sub('\\W', ' ', i)  # Remove non-word characters
        i = re.sub('\n', '', i)  # Remove newline characters
        i = re.sub(' +', ' ', i)  # Replace multiple spaces with a single space
        normalized.append(i)
    return normalized

# Load the tokenizer
tokenizer_path = 'tokenizer.json'  
with open(tokenizer_path, 'r') as f:
    tokenizer = tokenizer_from_json(f.read())

# Function to predict bipolarity
def predict_bipolarity(user_input):
    normalized_input = normalize([user_input])
    seq = tokenizer.texts_to_sequences(normalized_input)
    padded_seq = pad_sequences(seq, padding='post', maxlen=256)
    prediction = model.predict(padded_seq)
    probability = prediction[0][0]
    classification = "Bipolar" if probability > 0.5 else "Non-Bipolar"
    
    # Directly return a dictionary suitable for jsonify
    return {
        'probability': float(probability),  # Ensure it's a native Python float
        'classification': classification
    }

