from flask import make_response, jsonify


def response_handler(message, status_code=200, data=None):

    response = {
        "message": message,
        "status": "",
        "status_code": status_code,
        "data": data
    }

    if status_code >= 500:
        response["status"] = "INTERNAL_SERVER_ERROR"
    elif status_code >= 400:
        response["status"] = "BAD_REQUEST"
    elif status_code >= 300:
        response["status"] = "REDIRECT"
    elif status_code >= 200:
        response["status"] = "SUCCESS"
    else:
        response["status"] = "UNKNOWN"

    return make_response(
        jsonify(response),
        status_code
    )
