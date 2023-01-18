import json
from random import randint
from bson import json_util
from src.application.config.texts import love_text
from src.repositories.main import get_all_not_viewed


def get_a_new_love_text_use_case():
    not_viewed_texts = list(get_all_not_viewed())
    total_of_not_viewed_texts = len(not_viewed_texts)

    if total_of_not_viewed_texts:
        random_text = json.loads(json_util.dumps(not_viewed_texts[randint(0, total_of_not_viewed_texts - 1)]))['text']
        return random_text

    return love_text
