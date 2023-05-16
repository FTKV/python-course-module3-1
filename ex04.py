greeting = "Hello"

def print_greeting():
    #global greeting
    greeting = "Hello World"
    print(greeting)

print(globals())
print_greeting()
print(globals())