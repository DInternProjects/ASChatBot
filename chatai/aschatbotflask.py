"""
This module sets up a Flask web application to interact with
a locally running DeepSeek API for chatbot functionality.
"""

import os
import traceback  # Corrected import order
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests

# Load .env variables
load_dotenv()

app = Flask(__name__)

# Define the DeepSeek API endpoint (use the address provided by LM Studio)
DEEPSEEK_API_URL = os.getenv("API_ADDRESS")  # Update this to the correct endpoint

@app.route("/")
def welcome():
    """
    Displays the welcome screen with a redirect button to the chat interface.
    """
    return render_template("welcome.html")

@app.route("/chat")
def chat():
    """
    Renders the chat interface.
    """
    return render_template("chat.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    """
    Handles sending a user message to the locally running DeepSeek API
    and returning the response to the frontend.
    """
    try:
        # Get the user's message from the frontend
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Send the user's message to the DeepSeek API
        payload = {"prompt": user_message}

        # Added timeout argument to avoid hanging indefinitely
        response = requests.post(
            DEEPSEEK_API_URL,
            json=payload,
            timeout=10
        )
        response.raise_for_status()

        # Parse the DeepSeek API response
        response_data = response.json()
        bot_message = response_data.get("choices", [{}])[0].get(
            "text",
            "No response received from DeepSeek API."
        )
        # Return the bot's message to the frontend
        return jsonify({"message": bot_message})

    except requests.exceptions.RequestException as error:
        # Handle HTTP errors with DeepSeek API
        print("Error communicating with DeepSeek API:")
        traceback.print_exc()
        return jsonify({"error": f"Failed to connect to DeepSeek API: {error}"}), 500

    except (KeyError, TypeError) as error:
        # Handle specific potential exceptions
        print(f"Error parsing DeepSeek API response: {error}")
        traceback.print_exc()
        return jsonify({"error": f"Error processing API response: {error}"}), 500

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, port=8080)
