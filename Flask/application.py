# Done as part of Cs50x
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, date

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    #Initializes values
    stocks = db.execute("SELECT * FROM stocks WHERE user_id = ?", session["user_id"])
    finance = []
    symbols = db.execute("SELECT DISTINCT symbol FROM stocks WHERE user_id = ?", session["user_id"])
    cash = 10000

    #Iterates through shares
    for symbol in symbols:
        #Gets number of shares
        shares = db.execute("SELECT SUM(shares) FROM stocks WHERE user_id = ? AND symbol = ?", session["user_id"], symbol["symbol"])
        share = int(shares[0]["SUM(shares)"])

        #Gets data about shares
        symbol_data = lookup(symbol["symbol"])
        #Returns empty template if there are no shares
        if symbol_data is None:
            return render_template("index.html")

        else:
            name = symbol_data["name"]
            price = float(symbol_data["price"])
            total = round(price * share, 2)
            finance.append({
                "symbol": symbol["symbol"].upper(),
                "name": name,
                "price": price,
                "shares": share,
                "total": total
            })
            #Updates value of cash
            cash -= total

    #Updates user data
    db.execute("UPDATE users SET total = ? WHERE id = ?", cash, session["user_id"])
    return render_template("index.html", finance=finance, cash =round(cash, 2))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol").upper()
        #Checks if shares is a positive integer value
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("value must be a positive integer")
        if shares <= 0:
            return apology("value must be a positive integer")

        #Error checking
        if not symbol and shares:
            return apology("Please fill the required fields")

        #Gets data of the given symbol
        symbol_data = lookup(symbol)
        #Checks if symbol exists
        if symbol_data is None:
            return apology("Please recheck your symbol")

        #Gets total price of shares bought
        price = int(symbol_data["price"])
        total = price * shares

        #Checks if user has sufficient funds to buy the shares
        user_total_list = db.execute("SELECT total FROM users WHERE id = ?", session["user_id"])
        user_total = user_total_list[0]["total"]
        if total > user_total:
            return apology("Insufficient funds")
        else:
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            #Updates user data
            db.execute("INSERT INTO stocks(user_id,symbol,shares,price,date,time) VALUES(?,?,?,?,?,?)",
                        session["user_id"],symbol,shares,price,d1,current_time)
            return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    data = db.execute("SELECT * FROM stocks WHERE user_id = ? ORDER BY date DESC,time DESC",
                        session["user_idcheck50 cs50/problems/2021/x/finance"])
    return render_template("history.html",data=data)


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

        USER_ID = rows[0]["id"]

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
    if request.method == "GET":
        return render_template("quote.html")
    else:
        #Gets the data of the symbol
        symbol = request.form.get("symbol")
        symbol_data = lookup(symbol)

        #Checks if symbol exists
        if symbol_data is None:
            return apology("Recheck your symbol")
        else:
            return render_template("quoted.html", name=symbol_data["name"], symbol=symbol_data["symbol"], price=symbol_data["price"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        rc_password = request.form.get("confirmation")

        usernames = db.execute("SELECT username FROM users")
        print(usernames)
        #Error checking
        if not username:
            return apology("Please fill the required forms")
        elif not password:
            return apology("Please fill the required forms")
        elif not rc_password:
            return apology("Please fill the required forms")
        elif username in usernames:
            return apology("That username has already been taken")
        elif password != rc_password:
            return apology("Make sure your passwords match")

        #Updates user data if no errors
        try:
            key = db.execute("INSERT INTO users(username,hash) VALUES(:username,:password)",
                             username=username, password=generate_password_hash(password))
        except:
            return apology("username taken")
        return redirect("/login")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    #Gets user data(user id and the names of shares owned by them)
    user_id = session["user_id"]
    symbols = db.execute("SELECT DISTINCT symbol FROM stocks WHERE user_id = ?", user_id)
    symbols_list = []
    for symbol in symbols:
        symbols_list.append(symbol["symbol"])

    if request.method == "GET":
        return render_template("sell.html", symbols=symbols_list)
    else:
        #Gets number of shares owned by user
        stocks = {}
        for s in symbols:
            number = db.execute("SELECT SUM(shares) FROM stocks WHERE user_id = ? AND symbol = ?", user_id,s["symbol"])
            stocks.update({
                s["symbol"]: number[0]["SUM(shares)"]
            })

        symbol = request.form.get("symbol")
        share = int(request.form.get("shares"))

        #Error checking
        if symbol not in symbols_list:
            return apology("You do not own this stock")
        elif share > int(stocks[symbol]):
            return apology("Insufficient stocks")
        else:
            share = share - share * 2
            symbol_data = lookup(symbol)
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            #Updates user data
            db.execute("INSERT INTO stocks(user_id,symbol,shares,price,date,time) VALUES(?,?,?,?,?,?)",
                       session["user_id"], symbol, share, symbol_data["price"], d1, current_time)
            return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
