from blog import Flask
from blog import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

app.run()
