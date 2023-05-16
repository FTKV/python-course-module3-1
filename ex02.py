def print_greeting(name: str, age: int):
    if age >= 18:
        print(f"Hello, {name}")
    else:
        print("No entrance")

print_greeting("Bill", 20)
print_greeting(100, 30)