def class_logger(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            with open("output4.txt", "w", encoding="utf-8") as file:
                file.write(f"Створюється екземпляр класу {cls.__name__}\n")
            super().__init__(*args, **kwargs)
    return Wrapped

@class_logger
class ExampleClass:
    def __init__(self, value):
        self.value = value

instance = ExampleClass(42)

print("Результати записані у output4.txt")