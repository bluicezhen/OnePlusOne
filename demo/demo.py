from Niuniu import App, Resource
from Niuniu.dec.check import ParamRule, check_args


class ResourceHelloWorld(Resource):
    @check_args(param_rules=[ParamRule("test", int)])
    def post(self):
        return "hello world"


if __name__ == "__main__":
    app = App()
    app.add_resource("/hello_world", ResourceHelloWorld)
    app.run()
