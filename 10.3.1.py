def isIterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

objects = [123, "hello", [1, 2, 3], {"a": 1, "b": 2}, (4, 5), None]

with open("output1.txt", "w", encoding="utf-8") as file:
    for obj in objects:
        if isIterable(obj):
            file.write(f"Об'єкт {obj} підтримує ітераційний протокол\n")

print("Результати записані у output1.txt")