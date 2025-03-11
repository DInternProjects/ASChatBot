"""
This module contains the core Flask app for the chatbot application.
It sets up a connection to MongoDB and displays an example route.
"""

import os  # Standard library import
from flask import Flask  # Third-party imports
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = Flask(__name__)

# MongoDB connection
mongo_username = os.getenv('MONGODB_USERNAME')
mongo_password = os.getenv('MONGODB_PASSWORD')
mongo_uri = os.getenv('MONGO_URI')

@app.route("/")
def hello_world():
    """
    Displays the OpenAI API Key as an example route.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    return f"<p>Your OpenAI API Key: {api_key}</p>"

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, port=8080)
