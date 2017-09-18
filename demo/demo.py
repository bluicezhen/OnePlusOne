from OnePlusOne import App, Resource


class ResourceHelloWorld(Resource):
    def get(self):
        return "hello world"


if __name__ == "__main__":
    app = App()
    app.add_resource("/hello_world", ResourceHelloWorld)
    app.run()
