def greeting(name, age):
    name_upper = name.upper()
    birth_year = 2023 - age
    return name_upper, birth_year

print(__name__)

if __name__ == "__main__":
    print(type(greeting("Bill", 12)))

    result = greeting("Bill", 12)

    print(result)

    print(result[1])

    name, age = greeting("Bill", 12)

    print(name)
    print(age)