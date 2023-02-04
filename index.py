from flask import Flask, send_file, render_template

import json

app = Flask(__name__)

def load_title(video_name):
    with open("info.json", "r") as f:
        data = json.load(f)

    try:
        return data[video_name]["title"], data[video_name]["poster"]

    except IndexError:
        return "Not Available"


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/<video_name>")
def videot(video_name):
    title, poster = load_title(video_name)
    return render_template("video.html", title=title, video=video_name, poster=poster)
    

@app.route("/videos/<video_name>")
def video(video_name):
    return send_file(video_name)

app.run()