def class_logger(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            print(f"Створюється екземпляр класу {cls.__name__}")
            super().__init__(*args, **kwargs)
    return Wrapped

@class_logger
class ExampleClass:
    def __init__(self, value):
        self.value = value

instance = ExampleClass(42)