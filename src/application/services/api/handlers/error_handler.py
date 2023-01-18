from src.application.services.api.handlers.response_handler import response_handler
from src.application.config.texts import error_message


def error_handler(e):
    try:
        return response_handler(message=e.args[0], status_code=e.args[1])
    except IndexError:
        print(e)
        return response_handler(message=error_message, status_code=500)
