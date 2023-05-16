# def greeting(name: str, *numbers: int) -> str:
#     text = ""
#     # for i in numbers:
#     #     text += i + "\n"
#     return f"{name}: {numbers}"

# print(greeting("Bill", ["Bill", "Bill", "Bill"]))

# def greeting(name: str, *numbers: int) -> str:
#     text = ""
#     # for i in numbers:
#     #     text += i + "\n"
#     return f"{name}: {numbers}"

# print(greeting("Bill", *["Bill", "Bill", "Bill"]))

def greeting(name: str, *args) -> str:
    text = ""
    # for i in numbers:
    #     text += i + "\n"
    return f"{name}: {args}"

print(greeting("Bill", *["Bill", "Bill", "Bill"]))