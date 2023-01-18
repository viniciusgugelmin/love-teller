from pymongo import MongoClient
from src.application.config.environment import DATABASE_URL

mongo = MongoClient(DATABASE_URL)
db = mongo['test']

