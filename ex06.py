# def greeting(name: str, age: int) -> str:
#     return f"{name}: {age}"

# def greeting(name: str = "Bill", age: int) -> str: SyntaxError: non-default argument follows default argument
#     return f"{name}: {age}"

def greeting(name: str, age: int = 18) -> str:
    return f"{name}: {age}"

print(greeting(12, "Bill"))

print(greeting(name = "Bill"))