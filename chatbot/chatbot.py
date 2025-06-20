import json
import random
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer

# Download NLTK data (run once)
nltk.download('punkt')
nltk.download('punkt_tab')

lemmatizer = WordNetLemmatizer()

# Load your intents file (machine learning.json)
with open("machine_learning.json") as file:
    intents = json.load(file)

# Preprocess the data
words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        tokenized_words = nltk.word_tokenize(pattern)
        words.extend(tokenized_words)
        documents.append((tokenized_words, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(set(words))
classes = sorted(set(classes))

# Create bag of words
def bag_of_words(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

# Predict the intent
def predict_class(sentence):
    bow = bag_of_words(sentence)
    scores = []
    for intent in intents['intents']:
        match_score = np.dot(bow, bag_of_words(" ".join(intent['patterns'])))
        scores.append((intent['tag'], match_score))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return scores[0][0] if scores[0][1] > 0 else "no_match"

# Get a response from the matched intent
def get_response(intent_tag):
    for intent in intents['intents']:
        if intent['tag'] == intent_tag:
            return random.choice(intent['responses'])
    return "Sorry, I didn't understand that."

# Start chatbot loop
print("🤖 Chatbot is running! Type 'quit' to exit.\n")
while True:
    message = input("You: ")
    if message.lower() == "quit":
        print("Bot: Goodbye!")
        break
    intent = predict_class(message)
    response = get_response(intent)
    print("Bot:", response)

# Function used by the Flask app
def get_response_from_text(text):
    intent = predict_class(text)
    return get_response(intent)
