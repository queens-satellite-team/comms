import flask

app = flask.Flask(__name__)

@app.route("/")
def map():
    return flask.render_template('map.html')

@app.route("/stop")
def stop_server():
    func = flask.request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'