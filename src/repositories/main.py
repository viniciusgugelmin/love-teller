from datetime import datetime
from bson.objectid import ObjectId

from src.application.services.database.main import db


def get_all_not_viewed():
    return db['texts'].find({'viewed_at': None})


def get_specific_text(text: str):
    return db['texts'].find_one({'text': text})


def update_viewed_at(_id: str):
    db['texts'].update_one({'_id': ObjectId(_id)}, {'$set': {'viewed_at': datetime.utcnow()}})


def create(text: str):
    db['texts'].insert_one({'text': text, 'created_at': datetime.utcnow(), 'viewed_at': None})
