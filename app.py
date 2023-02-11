from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "n/a"


@app.route("/")
def index_route():
    return render_template("index.html", example_var="Hello, from backend!")


@app.route("/login", methods=["GET", "POST"])
def login_route():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(f"Attempting to login account: {email}")
        # TODO: Setup database & handle this request
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register_route():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        print(f"Attempting to register account: {username}")
        # TODO: Setup database & handle this request
    
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
