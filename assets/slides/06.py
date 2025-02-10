# Zero-args

y = lambda: 2*x
x = 3
y()
x = 4
y()

# Dice

from random import randint

def six_sided():
    return randint(1, 6)

def eight_sided():
    return randint(1, 8)

def d20():
    return randint(1, 20)

def repeats(n, dice):
    "Return how many times a dice roll is the same as the previous one in n rolls."
    count = 0
    previous = None
    while n:
        outcome = dice()
        print(outcome)
        if previous == outcome:
            count += 1
        previous = outcome
        n -= 1
    return count

# You haven't yet learned dictionaries or for loops,
# but this is similar to something you might do in DATA 8.
# display_histogram(six_sided)
def display_histogram(func, calls=50):
    # Dictionary to store counts of return values
    results = {}

    # Track function outputs
    count = 0
    while count < calls:
        value = func()
        results[value] = results.get(value, 0) + 1
        count += 1

    # Display histogram with sorted keys
    for key in sorted(results.keys()):
        stars = '*' * results[key]
        print(f"{key}: {stars}")


# Loops

def reprint(n):
    def a(word):
        k = n
        while k:
            print(word)
            k -= 1
    return a


# Lambdas

(lambda f: lambda x: f(f(x)))(lambda y: y * y)(3)

def twice(f):
    # g = lambda x: f(f(x))
    def g(x):
        return f(f(x))
    return g

square = lambda y: y * y

def square(y):
    return y * y



# snap = lambda chat: lambda: snap(chat)
# snap, chat = print, snap(2020)
# chat()
# chat()
