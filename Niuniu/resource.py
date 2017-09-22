from werkzeug.wrappers import Request


class Resource(object):
    def __init__(self, request: Request):
        self._request = request

        # Get HTTP search params (query string).
        self.args = {}
        for k, v in request.args.items():
            self.args[k] = v[0]
