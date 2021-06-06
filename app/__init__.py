from flask import Flask, render_template, request, url_for
import jinja2
import re
from urllib.parse import urlparse, parse_qs
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])

def homepage():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        url = request.form["url"]
        yt_url = urlparse(url)
        
        if yt_url.path[:9] == '/playlist':
                p_id = parse_qs(yt_url.query)['list'][0]
                return render_template('index.html', playlist_id = p_id)
        
        idRegex = re.compile(r'(?:\/|%3D|v=|vi=)([0-9A-z-_]{11})(?:[%#?&]|$)')
        v_id = idRegex.search(url)
        return render_template('index.html', youtube_id = v_id.group(1))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
