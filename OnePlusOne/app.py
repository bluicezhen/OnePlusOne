from werkzeug.serving import run_simple
from .server import Server


class App(object):
    def __init__(self):
        self.server = Server()

    def add_resource(self):
        pass

    def run(self):
        run_simple('0.0.0.0', 3773, self.server, use_debugger=True, use_reloader=True)
