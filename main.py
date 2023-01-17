from flask import *
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    data_set = {"data": "I love you"}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(port=7777)
