#. .venv/bin/activate


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, port=8080)

