from flask import Flask, render_template, request
import jinja2, re
from pytube import Playlist
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])

def homepage():

    if request.method == "GET":
        return render_template('index.html')

    if request.method == "POST":
        url = request.form["url"]
        try:
            idRegex = re.compile(r'(?:\/|%3D|v=|vi=)([0-9A-z-_]{11})(?:[%#?&]|$)')
            v_id = idRegex.search(url)
            if v_id:
                    return render_template('index.html', youtube_id = v_id.group(1))
            p = Playlist(url)
            idRegex = re.compile(r'(?:list=)([0-9A-z-_]{34})')
            p_id = idRegex.search(url)
            p_len = len(p.videos)
            p_v_ids = []
            for i in p.video_urls[:p_len]:
                idRegex = re.compile(r'(?:\/watch?v=|)([0-9A-z-_]{11})')
                v_id = idRegex.search(i)
                p_v_ids.append(v_id.group(1))
            return render_template('index.html', playlist_id = p_id.group(1) , p_title = p.title, v_ids = p_v_ids)
        except:
            error = "Something went wrong.Please enter valid URL."
            return render_template('index.html', error = error)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
