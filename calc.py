def add(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("We need a number!")
    else:
        return x+y

def minus(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("We need a number!")
    else:
        return x-y

def multiply(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("We need a number!")
    else:
        return x*y

def divide(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("We need a number!")
    if y == 0:
        raise ZeroDivisionError("We cant divide by 0")
    else:
        return x/y
