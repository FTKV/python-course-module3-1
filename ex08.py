def greeting(name: str, *numbers, **friends) -> str:
    return f"{name}: {numbers} {friends}"

print(greeting("Bill"))

print(greeting("Bill", 12, first_friend = "Dick", second_friend = "Sarah"))

print(greeting("Bill", 12, {"first_friend": "Dick", "second_friend": "Sarah"}))

print(greeting("Bill", 12, *{"first_friend": "Dick", "second_friend": "Sarah"}))

print(greeting("Bill", 12, **{"first_friend": "Dick", "second_friend": "Sarah"}))