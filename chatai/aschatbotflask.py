#. .venv/bin/activate


from flask import Flask
from dotenv import load_dotenv
import os

#load .env variables
load_dotenv()

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def hello_world():
    return f"<p>Your OpenAI API Key: {api_key}</p>"

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, port=8080)
