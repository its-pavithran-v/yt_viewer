from flask import Flask, render_template, request, url_for
import jinja2
from urllib.parse import urlparse, parse_qs
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def homepage():

    if request.method == "GET":
        return render_template('index.html')

    if request.method == "POST":
        url = request.form["url"]
        yt_url = urlparse(url)
        if yt_url.hostname == 'youtu.be':
            video_id = yt_url.path[1:]
            return render_template('index.html', youtube_id = video_id)
        if yt_url.hostname in {'www.youtube.com', 'youtube.com'}:
            if yt_url.path == '/watch':
                video_id = parse_qs(yt_url.query)['v'][0]
            if yt_url.path[:7] == '/watch/':
                video_id = yt_url.path.split('/')[1]
            if yt_url.path[:7] == '/embed/':
                video_id = yt_url.path.split('/')[2]
            if yt_url.path[:3] == '/v/':
                video_id = yt_url.path.split('/')[2]
            if yt_url.path[:9] == '/playlist':
                video_id = parse_qs(yt_url.query)['list'][0]
                return render_template('index.html', youtube_id = video_id , playlist = True)
            return render_template('index.html', youtube_id = video_id)
        else:
            return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
