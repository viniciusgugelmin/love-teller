from random import randint
from src.application.config.texts import love_text
from src.repositories.main import get_all_not_viewed, update_viewed_at
from src.utils.list_to_object import list_to_object


def get_a_new_love_text_use_case():
    not_viewed_texts = list(get_all_not_viewed())
    total_of_not_viewed_texts = len(not_viewed_texts)

    if total_of_not_viewed_texts:
        random_text_object = list_to_object(not_viewed_texts[randint(0, total_of_not_viewed_texts - 1)])
        update_viewed_at(random_text_object['_id']['$oid'])

        return random_text_object['text']

    return love_text
