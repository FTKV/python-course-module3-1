print(print("Hello World"))

def print_greeting(name: str, age: int) -> str:
    if age >= 18:
        return f"Hello, {name}"
    else:
        return "No entrance"
    
result = print_greeting("Bill", 40)

print(result)