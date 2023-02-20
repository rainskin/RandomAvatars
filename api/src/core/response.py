RESULT = list | str | int | bool


def make_response(result: RESULT) -> dict:
    return {'result': result}


OK = make_response(True)
