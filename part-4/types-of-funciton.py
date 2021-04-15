def greet(name):
    print(f"Hi {name}")
greet("Rafsan")


#  In programming, there are two types of functions.
# 1- perform a task ---> it means to print something on the screen.
# 2- Return a value  ---> kono efkta value refturn korbe.

# python a sob function  e by default "None" value return kore. jodi na specificly kono value return kora hoy.

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Rafsan Rifat")

print(message)