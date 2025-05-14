def log_function_name(func):
    def wrapper(*args, **kwargs):
        with open("output3.txt", "w", encoding="utf-8") as file:
            file.write(f"Викликається функція: {func.__name__}\n")
            result = func(*args, **kwargs)
            file.write(result + "\n" if result else "")
        return result
    return wrapper

@log_function_name
def example_function():
    return "Це приклад функції"

example_function()

print("Результати записані у output3.txt")