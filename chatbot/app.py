from flask import Flask, render_template, request, jsonify
from chatbot import get_response_from_text  # Make sure this exists

import threading
import webbrowser

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Ensure this file is inside a "templates" folder

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json().get("message")
    response = get_response_from_text(message)
    return jsonify({"answer": response})

# Function to open the browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True, port=5000, use_reloader=False)
