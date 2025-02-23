"""
Simple script to print the application version.

This script defines a version constant and provides an API endpoint
to return the version as a JSON response.
"""

from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "v0.0.1"

@app.route("/")
def home():
    """Returns a welcome message."""
    return "Welcome to the Versioning API. Try /version"

@app.route("/version")
def get_version():
    """Returns the application version as JSON."""
    return jsonify({"version": VERSION})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # Bind to all network interfaces
