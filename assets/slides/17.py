# Iterators

def iterator_demos():
    """Using iterators

    >>> s = [[1, 2], 3, 4, 5]
    >>> next(s)
    Traceback (most recent call last):
        ...
    TypeError: 'list' object is not an iterator
    >>> t = iter(s)
    >>> next(t)
    [1, 2]
    >>> next(t)
    3
    >>> u = iter(s)
    >>> next(u)
    [1, 2]
    >>> list(t)
    [4, 5]

    >>> a = [1, 2, 3]
    >>> b = [a, 4]
    >>> c = iter(a)
    >>> d = c
    >>> print(next(c))
    1
    >>> print(next(d))
    2
    >>> b
    [[1, 2, 3], 4]
    """

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

def built_in_demo():
    """Using built-in sequence functions.

    >>> bcd = ['b', 'c', 'd']
    >>> [x.upper() for x in bcd]
    ['B', 'C', 'D']
    >>> caps = map(lambda x: x.upper(), bcd)
    >>> next(caps)
    'B'
    >>> next(caps)
    'C'
    >>> s = range(3, 7)
    >>> doubled = map(double, s)
    >>> next(doubled)
    *** 3 => 6 ***
    6
    >>> next(doubled)
    *** 4 => 8 ***
    8
    >>> list(doubled)
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    >>> all(map(double, range(-3, 3)))
    *** -3 => -6 ***
    *** -2 => -4 ***
    *** -1 => -2 ***
    *** 0 => 0 ***
    False
    """


class myrange:
    def __init__(self, n, step=1):
        self.i = 0
        self.n = n
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            current = self.i
            self.i += self.step
            return current
        else:
            raise StopIteration()

class rangehof:
    """
    >>> x = rangehof(0, 3, lambda x: x+1)
    >>> list(x)
    [1, 2, 3]
    """
    def __init__(self, start, stop, function):
        self.i = start
        self.n = stop
        self.function = function

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            current = self.function(self.i)
            self.i = current
            return current
        else:
            raise StopIteration()
