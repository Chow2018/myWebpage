from flask import Flask, render_template, request, flash
from youtube_subtitle import getYouTubeTranscript
from test import getSomeText

app = Flask(__name__)

@app.route("/hello")
def index():
    return render_template("index.html")

@app.route("/youtubeSubtitle")
def youtubeSubtitle():
    return getYouTubeTranscript("Ngk09xRRzW8")