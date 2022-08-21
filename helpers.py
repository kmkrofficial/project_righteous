from flask import jsonify


def exceptionAsAJson(cause, e):
    return jsonify({
        "caused at": str(cause),
        "error": str(e)
    })


def successAsJson():
    return jsonify({
        "status": "success"
    })


def successAsJsonWithObj(obj):
    return jsonify({
        "status": "success",
        "object": obj
    })
