from werkzeug.wrappers import Response


class Server(object):
    def __call__(self, environ, start_response):
        response = Response('Hello World!')
        return response(environ, start_response)
