"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import logging

import arrow  # Replacement for datetime, based on moment.js
import flask
from flask import request

import acp_times  # brevet time calculations
import config


app = flask.Flask(__name__)
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
    """
    Calculates open/close times from km, using rules
    described at https://rusa.org/pages/acp-brevet-control-times-calculator.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)

    app.logger.debug(f"request.args: {request.args}")
    app.logger.debug(f"km={km}")

    # FIXME: These probably aren't the right open and close times and brevets may be longer than 200km
    #   they need more arguments from the front-end.
    open_time = acp_times.open_time(km, 200, arrow.now().isoformat)
    close_time = acp_times.close_time(km, 200, arrow.now().isoformat)
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.logger.info(f"Opening for global access on port {CONFIG.PORT}")
    app.run(port=CONFIG.PORT, host="0.0.0.0", debug=True)
