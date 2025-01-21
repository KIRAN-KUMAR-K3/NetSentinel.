from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def run_dashboard():
    print("Running web dashboard...")
    app.run(debug=True, port=5000)
