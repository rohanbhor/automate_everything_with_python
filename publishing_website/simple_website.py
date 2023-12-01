from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
  return "welcome to my website"


app.run(host="0.0.0.0")
