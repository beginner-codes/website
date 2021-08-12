from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("test.html")


@app.route("/test")
def index():
    return render_template("test2.html")


if __name__ == "__main__":
    app.run(debug=True)
