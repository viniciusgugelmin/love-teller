import json
from bson import json_util


def list_to_object(collection: list):
    return json.loads(json_util.dumps(collection))
