class CallCounter:
    def __init__(self):
        self.n = 0

    def count(self, f):
        def counted(n):
            self.n += 1
            return f(n)
        return counted

def iter_fib(n):
    first, second = 0, 1
    for _ in range(n):
        first, second = second, first+second
    return first

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

# memo is built into Python!
from functools import cache
faster_fib = cache(fib)
