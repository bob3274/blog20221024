from calendar import week
from flask import Flask, render_template, request, url_for, redirect
from json import load, dump
import time

app = Flask(__name__)

#date = time.strftime("%Y/%m/%d %H:%M", time.localtime())
with open("people.json") as f:
    aday = load(f)
    if time.strftime("%a", time.localtime()) != aday["week"]:
        aday["today"] = 0
        aday["week"] = time.strftime("%a", time.localtime())
        with open("people.json", "w") as f:
            dump(aday, f)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.values['send'] == '送出':
            return render_template('index.html', name=request.values['user'])
    return render_template('index.html', name="")


@app.route("/introduce", methods=['POST', 'GET'])
def introduce():
    with open("people.json") as f:
        people = load(f)
        people["today"] += 1
        people["total"] += 1
        with open("people.json", "w") as f:
            dump(people, f)
    if request.method == 'POST':
        if request.values['send'] == '送出':
            i = request.values.get('code')
            if len(i) == 10:
                a = int(int(i[0:4]) * 7 / 2 + 94 / 3)  # 4位亂數
                b = int(int(i[4:8]) * 9 / 6 + 83 / 1.5)  # 4位亂數
                c = chr(int(ord(i[8]) * 4 / 6 + 25))  # 65~90
                d = chr(int(ord(i[9]) * 1.5 / 1.3 - 17))  # 100~120
                i = str(a) + str(b) + c + d
                return render_template('introduce.html', verification=i, today=str(people["today"]), total=str(people["total"]))

    return render_template("introduce.html", verification="", today=str(people["today"]), total=str(people["total"]))


@app.route("/project")
def project():
    return render_template("project.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port='5000', debug=True)
