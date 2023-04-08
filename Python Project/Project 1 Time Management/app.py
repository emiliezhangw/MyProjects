from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Use sql to get the database
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///schedule.db")

# Make sure the response has been replied
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Default index html with two methods
@app.route("/", methods=["GET", "POST"])
def index():
    # Get new record details if the method is post
    if request.method == "POST":
        event = request.form.get("event")
        start = request.form.get("start_time")
        end = request.form.get("end_time")
        day = request.form.get("day")
        h1, m1 = start.split(":")
        h2, m2 = end.split(":")
        duration = (int(h2) - int(h1)) * 60 + int(m2) - int(m1)

        # Add the record to database as a new row
        if request.form.get("add"):
            db.execute("INSERT INTO time (event, start, end, weekday, duration) VALUES(?, ?, ?, ?, ?)",
                       event, start, end, day, duration)

            # If there is no row for current event, add a new record
            if len(db.execute("SELECT * FROM events WHERE event = ?", event)) != 0:
                event_time = db.execute("SELECT * FROM events WHERE event = ?", event)[0]['event_total']
                event_time_new = event_time + duration
                db.execute("UPDATE events SET event_total = ? WHERE event = ?",
                            event_time_new, event)
            # Else, update the original event time and total time
            else:
                db.execute("INSERT INTO events (event, event_total) VALUES(?, ?)",
                        event, duration)

            total = db.execute("SELECT * FROM events")[0]['total']
            db.execute("UPDATE events SET total = ?", total + duration)
            flash("Add successfully!")

        # Drop records as user need
        elif request.form.get("drop"):
            if len(db.execute("SELECT * FROM time WHERE event = (?) and start = (?) and end = (?) and weekday = (?)", event, start, end, day)) != 0:
                db.execute("DELETE FROM time WHERE event = (?) and start = (?) and end = (?) and weekday = (?)",
                        event, start, end, day)
                total = db.execute("SELECT * FROM events")[0]['total']
                db.execute("UPDATE events SET total = ?", total - duration)
                flash("Drop successfully!")
            else:
                flash("Record do no exist!")
        return render_template("index.html")

    # redirect to index.html if the method is get
    else:
        return render_template("index.html")


@app.route("/activity")
def activity():
    details = db.execute("SELECT * FROM time")
    return render_template("activity.html", details=details)


@app.route("/analyse")
def analyse():
    events = db.execute("SELECT * FROM events")
    if len(events) != 0:
        return render_template("analyse.html", events=events)
    else:
        return render_template("index.html")
