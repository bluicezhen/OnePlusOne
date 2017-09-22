## Niuniu

**A web RESTFul framework simple as 1+1.**

## 1. Setup

    pip install Niuniu

## 2. simple demo

```python
from Niuniu import App, Resource


class ResourceHelloWorld(Resource):
    def get(self):
        return "hello world"


if __name__ == "__main__":
    app = App()
    app.add_resource("/", ResourceHelloWorld)
    app.run()
```

You can visit http://localhost:3773 to see 'hello world'.