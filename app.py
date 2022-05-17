from flask import Flask, render_template, request, flash
from youtube_subtitle import getYouTubeTranscript
from test import getSomeText
import json

app = Flask(__name__)

@app.route("/hello")
def index():
    return render_template("index.html")

@app.route("/youtubeSubtitle")
def youtubeSubtitle():
    return getYouTubeTranscript("Ngk09xRRzW8")

@app.route("/youtubeSubtitle2/<url>")
def youtubeSubtitle2(url):
    subtitle = {
        "url": url,
        "text": getYouTubeTranscript(url)    
    } 
    return json.dumps(subtitle)