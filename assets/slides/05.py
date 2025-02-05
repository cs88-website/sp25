# Functional arguments

def twice(f, x):
    """Return f(f(x))

    >>> twice(square, 2)
    16
    >>> from math import sqrt
    >>> twice(sqrt, 16)
    2.0
    """
    return f(f(x))

def square(x):
    return x * x

result = twice(square, 2)

# Summation

def cube(x):
    return pow(x, 3)

def identity(x):
    return x

def summation(x, term):
    """
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total = total + term(k)
        k = k + 1
    return total

# Functional return values

def make_adder(n):
    """Return a function that takes one argument k and returns k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

# Lambda (Fall 2022 Midterm 1)

twice(lambda y: y+y, 3)

bear = -1
oski = lambda print: print(bear)
bear = -2
oski(abs)

# Curry

"""
>>> curry = lambda f: lambda x: lambda y: f(x, y)
>>> reverse = lambda g: lambda x, y: g(y, x)
>>> square = curry(reverse(pow))(2)
"""

def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def reverse(g):
    def h(x, y):
        return g(y, x)
    return h

square = curry(reverse(pow))(2)

# Env Diagram

# def f(x):
#     """f(x)(t) returns max(x*x, 3*x)
#     if t(x) > 0, and 0 otherwise.
#     """
#     y = max(x * x, 3 * x)
#     def zero(t):
#         if t(x) > 0:
#             return y
#         return 0
#     return zero

# y = 1
# while y < 10:
#     if f(y)(lambda z: z - y + 10):
#         max = y
#     y = y + 1
