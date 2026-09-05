from flask import Flask, render_template
from source import maps

app = Flask(__name__,
    static_folder="static",
    static_url_path="/static"
    )

@app.route("/")
def hello_world():
    return render_template("index.html", datamaps=maps)

@app.route("/map/<m_name>")
def map_viewer(m_name):
    return render_template("floors.html", map=maps[m_name])