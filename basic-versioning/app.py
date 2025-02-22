from flask import Flask

app = Flask(__name__)

VERSION = "v0.0.1"

@app.route("/version")
def version():
    """Returns the application version."""
    return {"version": VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # Keeps the process running!
