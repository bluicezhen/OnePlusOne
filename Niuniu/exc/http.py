from werkzeug.exceptions import HTTP_STATUS_CODES


class ExceptionHTTP(Exception):
    def __init__(self, code: int, desc: str = None):
        self.code = code
        if desc:
            self.desc = desc
        else:
            try:
                self.desc = HTTP_STATUS_CODES[code]
            except KeyError:
                self.code = 500
                self.desc = HTTP_STATUS_CODES[500]
