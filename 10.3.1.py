def isIterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

objects = [123, "hello", [1, 2, 3], {"a": 1, "b": 2}, (4, 5), None]

for obj in objects:
    if isIterable(obj):
        print(f"Об'єкт {obj} підтримує ітераційний протокол")