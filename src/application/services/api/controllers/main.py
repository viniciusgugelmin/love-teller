from src.application.services.api.handlers.response_handler import response_handler
from src.application.config.texts import successful_message
from src.useCases.get_a_new_love_text_use_case import get_a_new_love_text_use_case


def main():
    data = get_a_new_love_text_use_case()

    return response_handler(
        message=successful_message,
        data=data
    )
