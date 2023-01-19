from src.repositories.main import create, get_specific_text
from src.application.config.environment import SECRET_PASSWORD


def create_a_new_love_text_use_case(text: str, password: str):
    if password != SECRET_PASSWORD:
        raise Exception('Invalid password', 401)

    text_already_exists = get_specific_text(text)

    if text_already_exists:
        raise Exception('This text already exists', 400)

    create(text)
