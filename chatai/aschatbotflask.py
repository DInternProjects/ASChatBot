from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

app = Flask(__name__)

# MongoDB connection
mongo_username = os.getenv('MONGODB_USERNAME')
mongo_password = os.getenv('MONGODB_PASSWORD')
mongo_uri = os.getenv('MONGODB_URI')

# Example route to display OpenAI API Key (to match your current setup)
api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def hello_world():
    return f"<p>Your OpenAI API Key: {api_key}</p>"

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, port=8080)
