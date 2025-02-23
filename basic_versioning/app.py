"""
Simple script to print the application version.

This script defines a version constant and provides API endpoints
to return the version as a JSON response.
"""

from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)

# Define the application version
VERSION = "v0.0.1"


@app.route("/")
def home():
    """
    Returns a welcome message.

    This helps users understand the API and directs them to the correct endpoint.
    """
    return "Welcome to the Versioning API. Try /version"


@app.route("/version")
def get_version():
    """
    Returns the application version as a JSON response.

    This allows clients to retrieve the version programmatically.
    """
    return jsonify({"version": VERSION})


if __name__ == "__main__":
    # Run the Flask application on port 5001, accessible from any network interface.
    app.run(host="127.0.0.1", port=5001)

