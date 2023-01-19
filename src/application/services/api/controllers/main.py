from flask import request

from src.application.services.api.handlers.response_handler import response_handler
from src.application.config.texts import successful_message
from src.useCases.get_a_new_love_text_use_case import get_a_new_love_text_use_case
from src.useCases.create_a_new_love_text_use_case import create_a_new_love_text_use_case


def main_get():
    data = get_a_new_love_text_use_case()

    return response_handler(
        message=successful_message,
        data=data
    )


def main_post():
    data = None
    try:
        data = request.get_json()
    except Exception as e:
        raise Exception('No data was sent', 400)

    if 'text' not in data:
        raise Exception('No text was sent', 400)

    if 'password' not in data:
        raise Exception('No password was sent', 400)

    create_a_new_love_text_use_case(data['text'], data['password'])

    return response_handler(
        message=successful_message,
        status_code=201
    )
