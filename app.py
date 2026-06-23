from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "CI/CD with GitHub Actions + AWS ECR",
        "version": "1.0.0",
        "timestamp": str(datetime.datetime.now()),
        "author": "Prasad Sonar"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
