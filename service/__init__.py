"""
Package: service
Package for the application models and service routes
This module creates and configures the Flask app and sets up the logging
and SQL database
"""
import logging
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

# Create Flask application
app = Flask(__name__)
talisman = Talisman(app)
CORS(app)

app.config.from_object("service.config")

# Import the routes After the Flask app is created
from service import routes, models
from service.common import error_handlers, cli_commands

# Set up logging for production
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

try:
    models.db.init_app(app)  # make our sqlalchemy tables
except Exception as error:  # pylint: disable=broad-except
    app.logger.critical("%s: Cannot continue", error)
    # gunicorn requires exit code 4 to stop spawning workers when they die
    sys.exit(4)

app.logger.info("Service initialized!")
