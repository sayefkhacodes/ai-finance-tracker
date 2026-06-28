from flask import Flask, render_template
from summary import get_summary

app = Flask(__name__)

@app.route("/")
def index():
    summary = get_summary()
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)