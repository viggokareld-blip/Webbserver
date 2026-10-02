from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    try:
        with open("inlagg.txt", "r", encoding="utf-8") as fil:
            inlagg = fil.readlines()
    except FileNotFoundError:
        inlagg = []

    return render_template("index.html", inlagg=inlagg)

@app.route("/skicka", methods=["POST"])
def skicka():
    namn = request.form["namn"]
    meddelande = request.form["meddelande"]
    tid = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("inlagg.txt", "a", encoding="utf-8") as fil:
        fil.write(f"{tid} | {namn}: {meddelande}\n")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)