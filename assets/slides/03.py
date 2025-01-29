# Print and None

# Options A, B, C

def triple(x):
    return 3 * x # versus print(3 * x)

f = triple

# # Try with strings.
# def greet(x):
#     return 'Hello, ' + x
# f = greet

def h_a(x):
    return print(f(x))

def h_b(x):
    print(f(x))
    return f(x)

def h_c(x):
    y = f(x)
    print(y)
    return y

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

def h(x):
    """
    >>> h(2)
    3
    3
    >>> f = print
    """
    y = f(x)
    print(y)
    return y

# Conditional Examples
# Try varying the value of x,
# The try running `python3 03.py` in your terminal.
x = -1
# if x > 2:
#     print('big')
# if x > 0:
#     print('positive')

# if x > 2:
#     print('big')
# elif x > 0:
#     print('less big')

if x > 2:
    print('big')
elif x > 0:
    print('less big')
else:
print('not pos')


# Prime factorization

def prime_factors(n):
    """Print the prime factors of positive integer n
       in non-decreasing order.

    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_factor(n)
        print(k)
        n = n // k

def smallest_factor(n):
    """Return the smallest factor of n greater than 1."""
    k = 2
    while n % k != 0:
        k = k + 1
    return k

# Repeating

def repeating(t, n):
    """Return whether t digits repeat to form positive integer n.

    >>> repeating(1, 6161)
    False
    >>> repeating(2, 6161)  # repeats 61 (2 digits)
    True
    >>> repeating(3, 6161)
    False
    >>> repeating(4, 6161)  # repeats 6161 (4 digits)
    True
    >>> repeating(5, 6161)  # there are only 4 digits
    False
    """
    if pow(10, t-1) > n:  # make sure n has at least t digits
        return False
    rest = n
    while rest:
        if rest % pow(10, t) != n % pow(10, t):
            return False
        rest = rest // pow(10, t)
    return True
