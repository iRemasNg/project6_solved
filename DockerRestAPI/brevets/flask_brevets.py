"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)
"""

import flask
from flask import request
from pymongo import MongoClient
import logging
import arrow  
import acp_times  
import config

app = flask.Flask(__name__)

# client = MongoClient(host="brevets_mongodb", port=27017)
# db = client.brevetsdb

HOSTNAME = "mongodb_host"
DATABASE_NAME = "brevets_db"
COLLECTION_NAME = "brevets"

client = MongoClient(host=HOSTNAME, port=27017)
db = client[DATABASE_NAME][COLLECTION_NAME]

CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('brevets.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


@app.route("/_calc_times")
def _calc_times():

    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    app.logger.debug(f"request.args: {request.args}")
    app.logger.debug(f"km={km}")

    brevet_dist = request.args.get('brevet_dist', 0, type=int)
    begin_date = request.args.get('begin_date', "", type=str)
    begin_time = request.args.get('begin_time', "", type=str)
    brevet_start_time = arrow.get(begin_date + " " + begin_time, 'YYYY-MM-DD HH:mm')
    open_time = acp_times.open_time(km, brevet_dist, brevet_start_time)
    close_time = acp_times.close_time(km, brevet_dist, brevet_start_time)

    result = {"open": arrow.get(open_time).format('ddd M/D H:mm'), "close": arrow.get(close_time).format('ddd M/D H:mm')}
    return flask.jsonify(result=result)


@app.route('/display', methods=['POST'])
def display():
    _items = db.find()
    items = [item for item in _items]

    return flask.render_template('display.html', items=items)


@app.route('/new', methods=['POST'])
def new():
    openInfo = request.form.getlist("open")
    closeInfo = request.form.getlist("close")
    kmInfo = request.form.getlist("km")

    siftedO = [str(item) for item in openInfo if str(item) != ""]
    siftedC = [str(item) for item in closeInfo if str(item) != ""]
    siftedK = [str(item) for item in kmInfo if str(item) != ""]

    length = max(len(siftedO), len(siftedC), len(siftedK))

   
    if length == 0:
        return flask.render_template('emptySubmit.html')

    for i in range(length):
        item_doc = {
            'km': siftedK[i] if i < len(siftedK) else "",
            'open': siftedO[i] if i < len(siftedO) else "",
            'close': siftedC[i] if i < len(siftedC) else ""
        }
        db.insert_one(item_doc)

    return flask.redirect(flask.url_for('index'))


app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
