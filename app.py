from flask import Flask, render_template, session, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


# This Modified alchemy class fixes: psycopg2.OperationalError: SSL connection has been closed unexpectedly
class SQLAlchemy(_BaseSQLAlchemy):
    def apply_pool_defaults(self, app, options):
        options = super().apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True
        return options


# Initialize flask application & configuration variables
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/wi5dom"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "n/a"

# Initialize database variables
db = SQLAlchemy()
db.init_app(app)


class UserAccount(db.Model):
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
    # Define database variables
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    username = db.Column(db.Text)
    password = db.Column(db.Text)


@app.route("/")
def index_route():
    if session.get("logged-in"):
        return render_template("index.html", username=session["username"], account_status="Logged in as {}".format(session["username"]))

    return render_template("index.html", account_status="Not logged in")


@app.route("/login", methods=["GET", "POST"])
def login_route():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(f"Attempting to login account: {email}")

        sql_query = db.session.execute(
            "select id,username,password from user_account where email='{}'".format(email))

        db_account = sql_query.first()
        if db_account:
            print("Account {} found, checking password.".format(email))
            id = db_account[0]
            username = db_account[1]
            db_password = db_account[2]
            if check_password_hash(db_password, password):
                print("Correct password for account: {}".format(email))
                # Initialize session variables. This allows the front-end page to interact with our logged-in account.
                session["logged-in"] = True
                session["id"] = id
                session["email"] = email
                session["username"] = username
                return redirect(url_for("index_route"))

        # Render template after login post, we default to error message
        return render_template("login.html", login_error_message="Error: Invalid username or password.", email=email)

    # Render template when we load the page the 1st time
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register_route():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        salted_password = generate_password_hash(password)

        print(f"Attempting to register account: {username}")
        # Check if username in use
        sql_query = db.session.execute(
            "select id from user_account where username='{}'".format(username))

        if sql_query.first():
            print("Account with this username already exists: {}".format(username))
            return render_template("register.html",
                                   register_error_message="Error: Username already in use.", email=email)

        # Check if email already in use
        sql_query = db.session.execute(
            "select id from user_account where email='{}'".format(email))

        if sql_query.first():
            print("Account with this email already exists: {}".format(username))
            return render_template("register.html",
                                   register_error_message="Error: Email already in use.", username=username)

        user = UserAccount(email, username, salted_password)
        db.session.add(user)
        db.session.commit()

        # TODO: Setup database & handle this request

    return render_template("register.html")


@app.route("/logout", methods=["POST"])
def logout_account():
    print("Logout")
    session.pop("logged-in")
    session.pop("id")
    session.pop("username")
    session.pop("email")
    return ""


if __name__ == "__main__":
    app.run(debug=True)
