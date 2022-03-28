import flask

app = flask.Flask(__name__)


@app.route("/")
def main():
    print("mustafa")
    return flask.render_template("index.html")