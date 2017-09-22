from Niuniu import App, Resource
from Niuniu.dec.check import ParamRule, check_args


class ResourceHelloWorld(Resource):
    @check_args(param_rules=[ParamRule("aaa", int)])
    def get(self):
        print(self.args)
        return "hello world"


if __name__ == "__main__":
    app = App()
    app.add_resource("/hello_world", ResourceHelloWorld)
    app.run()
