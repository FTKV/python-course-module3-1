def greeting(name):
    return f"Hello {name}"

def select_greet(name, func):
    return func(name)

print(select_greet("Bill", greeting))