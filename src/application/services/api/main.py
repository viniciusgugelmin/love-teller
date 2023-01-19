from flask import Flask, request

from src.application.services.api.controllers.main import main_get, main_post
from src.application.services.api.handlers.error_handler import error_handler

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.errorhandler(Exception)
def error_handler_function(e):
    return error_handler(e)


@app.route('/', methods=['GET', 'POST'])
def main_function():
    if request.method == 'GET':
        return main_get()

    if request.method == 'POST':
        return main_post()
