def log_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Викликається функція: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function_name
def example_function():
    print("Це приклад функції")

example_function()