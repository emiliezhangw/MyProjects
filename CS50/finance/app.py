import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    portfolio = db.execute("SELECT * FROM portfolio where userid = ?", session["user_id"])
    price = {}
    for stock in portfolio:
        price[stock['symbol']] = lookup(stock['symbol'])['price']
    return render_template("index.html", portfolio=portfolio, price=price, cash=db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["cash"])


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("MISSING SYMBOL", 400)
        if not shares:
            return apology("MISSING SHARES", 400)
        if not lookup(symbol):
            return apology("INVALID SYMBOL", 400)
        if not shares.isdigit() or int(shares) < 0:
            return apology("must provide a positive integer", 400)

        price = lookup(symbol)['price']
        cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        if float(cash) < price * int(shares):
            return apology("Oh, you cannot afford the number of shares at the current price", 400)

        cash -= int(shares) * price

        db.execute("INSERT INTO buy (userid, symbol, name, shares, price, total, cash) VALUES(?, ?, ?, ?, ?, ?, ?)",
                   session["user_id"], lookup(symbol)['symbol'], lookup(symbol)['name'], shares, price, int(shares) * price, cash)

        if len(db.execute("SELECT * FROM portfolio WHERE userid = ? AND name = ?", session["user_id"], lookup(symbol)['name'])) != 0:
            shares_before = db.execute("SELECT * FROM portfolio WHERE userid = ? AND name = ?",
                                       session["user_id"], lookup(symbol)['name'])[0]['shares']
            shares_new = shares_before + int(shares)
            total_new = shares_new * price
            db.execute("UPDATE portfolio SET shares = ?, cash = ?, total = ? WHERE userid = ?",
                       shares_new, cash, total_new, session["user_id"])
        else:
            db.execute("INSERT INTO portfolio (userid, symbol, name, shares, price, total, cash) VALUES(?, ?, ?, ?, ?, ?, ?)",
                       session["user_id"], lookup(symbol)['symbol'], lookup(symbol)['name'], shares, price, int(shares) * price, cash)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        flash("Bought!")
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM buy WHERE userid = ?", session["user_id"])

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        share = lookup(symbol)
        if not symbol:
            return apology("MISSING SYMBOL", 400)
        if not share:
            return apology("MISSING SHARES", 400)
        return render_template("quoted.html", share=share)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        session.clear()
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username:
            return apology("must provide username", 400)
        if not password:
            return apology("must provide password", 400)
        if password != confirmation:
            return apology("passwords do not match", 400)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 0:
            return apology("username already exists", 400)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))
        flash("Registered!")
        session["user_id"] = db.execute("SELECT * FROM users WHERE username = ?", username)[0]["id"]
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    portfolio = db.execute("SELECT * FROM portfolio where userid = ?", session["user_id"])

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("MISSING SYMBOL", 400)
        if not shares:
            return apology("MISSING SHARES", 400)
        shares_new = db.execute("SELECT * FROM portfolio WHERE symbol = ? AND userid = ?",
                                lookup(symbol)['symbol'], session["user_id"])[0]['shares'] - int(shares)
        if shares_new < 0:
            return apology("TOO MANY SHARES", 400)

        price = lookup(symbol)['price']
        cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        cash += int(shares) * price
        total_new = shares_new * price

        db.execute("INSERT INTO buy (userid, symbol, name, shares, price, total, cash) VALUES(?, ?, ?, ?, ?, ?, ?)",
                   session["user_id"], lookup(symbol)['symbol'], lookup(symbol)['name'], -int(shares), price, int(shares) * price, cash)

        db.execute("UPDATE portfolio SET shares = ?, cash = ?, total = ? WHERE userid = ? AND name = ?",
                   shares_new, cash, total_new, session["user_id"], lookup(symbol)['name'])

        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        flash("Sell!")
        return redirect("/")
    else:
        return render_template("sell.html", portfolio=portfolio)
