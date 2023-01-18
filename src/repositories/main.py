from src.application.services.database.main import db


def get_all_not_viewed():
    return db['texts'].find({'viewed_at': None})
