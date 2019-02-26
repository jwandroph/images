from flask import Flask, jsonify, render_template
import urllib3
import json

app = Flask(__name__)

link = "https://www.dropbox.com/s/a0azxc0mt7kma1n/camera_data.json?raw=1"
http = urllib3.PoolManager()
r = http.request('GET', link)
data = json.loads(r.data.decode('utf-8'))


@app.route("/")
def main():

    return render_template("main.html", cameras=data["camera_data"], wheel=data["wheel"], grid=data["grid"])


@app.route("/json")
def get_json():
    return jsonify(data)


if __name__ == "__main__":
    app.run(port=4954, debug=True)