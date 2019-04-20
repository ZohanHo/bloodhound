""""""
"""decorator как функция"""

def function1():
    print("text function1")

def decorator(f):
    def wrapper():
        print("after")
        f()
        print("before")
    return wrapper

function1 = decorator(function1)


"""decorator"""

def decorator(f):
    def wrapper():
        print("after")
        f()
        print("before")
    return wrapper

@decorator # Декоратор принимает function2 как параметр и декорирует ее
def function2():
    print("text function2")


"""decorator с ргументами"""

def decorator(f):
    print("after")
    def wrapper():
        f(5, 10)
        print("before")
    return wrapper

# Декоратор принимает function3 как параметр и декорирует ее c аргументами которые нужно передать в декоратор
@decorator
def function3(x, y):
    print(x + y)


"""decorator с ргументами"""
def decorator(f):
    print("after")
    def wrapper(a, b):
        f(a, b)
        print("before")
    return wrapper

# Декоратор принимает function4 как параметр и декорирует ее c аргументами которые нужно передать в декоратор
# или при вызове, но wrapper должна их знать
@decorator
def function4(x, y):
    print(x + y)


if __name__ == "__main__":
    function1()
    print("---------------next function-------------")
    function2()
    print("---------------next function-------------")
    function3()
    print("---------------next function-------------")
    function4(10, 20)