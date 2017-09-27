from werkzeug.wrappers import Request
from typing import Dict, Any
import json


class Resource(object):
    def __init__(self, request: Request):
        self._request = request

        # Get HTTP search params (query string).
        self._args = {}
        for k, v in request.args.items():
            self._args[k] = v[0]

        if request.content_type == "application/json":
            # If HTTP Content Type = "application/json", convert HTTP body (JSON string) to dict.
            charset = request.charset if request.charset else 'utf-8'
            self._json = json.loads(request.data.decode(charset))

    def get_args(self) -> Dict[str, Any]:
        """ Get HTTP search params (query string) """
        return self._args
