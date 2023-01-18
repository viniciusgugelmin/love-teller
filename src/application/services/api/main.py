from flask import Flask

from src.application.services.api.controllers.main import main
from src.application.services.api.handlers.error_handler import error_handler

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.errorhandler(Exception)
def error_handler_function(e):
    return error_handler(e)


@app.route('/', methods=['GET'])
def main_function():
    return main()
