class DynamicClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

attributes = {"name": "Python", "greet": lambda self: f"Hello, {self.name}!"}
NewClass = type("NewClass", (object,), attributes)

instance = NewClass()
print(instance.greet())