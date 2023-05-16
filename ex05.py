# def print_greeting():
#     greeting = "Hello"
#     print(greeting)

#     def local_greeting():
#         nonlocal greeting
#         print(greeting)

#     local_greeting()

# print_greeting()

greeting = "Hello"

def greeting():
    greeting = "Hello"
    print(greeting)

    def local_greeting():
        #global greeting
        greeting = "Hello World"
        print(greeting)

        def sub_local_greeting():
            nonlocal greeting
            print(greeting)

        sub_local_greeting()

    local_greeting()

greeting()