import torch
from transformers import pipeline

# Load the pre-trained hate speech detection model
classifier = pipeline("sentiment-analysis", model="user/roberta-large-finetuned-hate-speech")

def detect_hate_speech(text):
    # Use the pre-trained model to classify sentiment (hate speech or not)
    result = classifier(text)[0]

    # Get the label and score
    label = result['label']
    score = result['score']

    return label, score

if _name_ == "_main_":
    # Example usage
    text_input = input("Enter a text: ")
    label, score = detect_hate_speech(text_input)

    print(f"Label: {label}")
    print(f"Score: {score}")