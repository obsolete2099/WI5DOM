from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index_route():
    return render_template("index.html",example_var="Hello, from backend!")

@app.route("/login")
def login_route():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)