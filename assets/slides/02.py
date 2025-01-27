# Assignment

def ex():
    """
    >>> pow(2, 10)
    1024
    >>> max = pow
    >>> pow(2, 10)
    1024
    >>> pow = max
    >>> pow(2, 10)
    1024
    >>> max = pow
    >>> pow(2, 10)
    1024

    >>> def g(y):
    ...     x = 2 * y
    ...     return x + 1
    ... 
    >>> x = 2
    >>> g(x)
    5
    >>> g(3 * x) + 3
    16
    >>> x
    2
    >>> y = 3
    >>> g(y)
    7
    >>> y
    3
    """

# https://pythontutor.com/cp/composingprograms.html#code=def%20g%28y%29%3A%0A%20%20%20%20x%20%3D%202%20*%20y%0A%20%20%20%20return%20x%20%2B%201%0A%20%20%20%20%0Ax%20%3D%202%0Aprint%28g%28x%29%29%0Aprint%28g%283%20*%20x%29%20%2B%203%29%0A&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Name conflicts

from operator import mul

def square(square):
    return mul(square, square)
square(3)

# https://pythontutor.com/cp/composingprograms.html#code=from%20operator%20import%20mul%0Adef%20square%28square%29%3A%0A%20%20%20%20return%20mul%28square,%20square%29%0Aprint%28square%283%29%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Multiple Assignment

def diff(x, y):
    """
    >>> def diff(x, y):
    ...     x, y = y, x
    ...     return y - x
    
    >>> x, y = 6, 1
    >>> x, y = y, x-y
    >>> diff(y, x)
    4
    """
    x, y = y, x
    return y - x
    
# https://pythontutor.com/cp/composingprograms.html#code=def%20diff%28x,%20y%29%3A%0A%20%20%20%20x,%20y%20%3D%20y,%20x%0A%20%20%20%20return%20y%20-%20x%0A%20%20%20%20%0Ax,%20y%20%3D%206,%201%0Ax,%20y%20%3D%20y,%20x-y%0Aprint%28diff%28y,%20x%29%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Print and None

def triple(x):
    return x # versus print(x)

def noisy(x):
    """
    >>> noisy(noisy(2) + noisy(3))
    NOISY 2
    NOISY 3
    NOISY 7
    8
    """
    print('NOISY', x)
    return x + 1
