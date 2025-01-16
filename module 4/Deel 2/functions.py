def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def increase(a):
    return a + 1

def decrease(a):
    return a - 1

def double(a):
    return a * 2

def half(a):
    return a / 2

CALCULATIONS = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b,
    "increase": lambda a: a + 1,
    "decrease": lambda a: a - 1,
    "double": lambda a: a * 2,
    "half": lambda a: a / 2
}