
text = "Hello, C88C!"
# for letter in text:
#     print(letter)

def sum_to_n(n):
    total = 0
    for num in range(0, n + 1):
        total += num
    return total

def sum_to_n_down(n):
    total = 0
    for num in range(n, 0, -1):
        total += num
    return total

sum(range(0, 11))

def sum_to_n(n):
    return sum(range(0, n + 1))

text = 'Hello, C88C!'
len(text)
text.count('l')
text.count(8)
text.count('8')

courses = ['DATA C88C', 'DATA 8', 'POLSCI 2', 'MATH 54']

list(range(0, 11))

numbers = [ x for x in range(11) ]

numbers = [2 ** x for x in range(10) ]

courses[0]
courses[0].split(' ')
[ c.split(' ') for c in courses ]


# Lists practice

digits = [1, 8, 2, 8]
8 in digits
[1, 8] in digits
1 in digits and 8 in digits

# for x in digits:
#     continue
#     #print(100 * x)

def f(x):
    for y in [x, x + 1, x + 2]:
        print('this is y:', y)
        if y > 0:
            return y
    return 1000

def print_negatives(s):
    for d in s:
        d = -d
        print(d)
    print(s)
    s = [2, 3, 4]
    return s

# Range practice

def range_practice():
    range(4)
    list(range(4))
    range(-2, 2)
    list(range(-2, 2))
    range(2, 100000000)  # 9 zeroes slows things down a lot
    list(range(2, 100000000))
    len(range(2, range(0, 23)[9]))

def fib(n):
    """Return the nth fibonnaci number.

    >>> fib(0)
    0
    >>> fib(2)
    1
    >>> fib(10)
    55
    """
    fib_number = 0
    what_to_add = 1  # to get to the next fib number
    for _ in range(n):
        what_to_add, fib_number = fib_number, fib_number + what_to_add
    return fib_number

# List comprehension practice

xs = range(-10, 11)
ys = [x*x - 2*x + 1 for x in xs]

xs_where_y_is_below_10 = [x for x in xs if x*x - 2*x + 1 < 10]
xs_where_y_is_below_10 = [xs[i] for i in range(len(xs)) if ys[i] < 10]

# Optional Tree recursion practice

goal = 21

def play(strategy0, strategy1, n=0, who = 0, announce=False):
    "Play twenty-one starting at n and return the index of the winner."
    strategies = [strategy0, strategy1]
    while n < goal:
        n = n + strategies[who](n)
        if announce:
            print('Player', who, 'increases n to', n)
        who = 1 - who
    return who

def two_strat(n):
    "Always choose 2."
    return 2

def interactive(n):
    "Ask the user."
    choice = input('Pick 1, 2, or 3: ')
    if choice in ['1', '2', '3']:
        return int(choice)
    else:
        print('Invalid choice!')
        return interactive(n)

def best(n, other_strategy):
    """Return an best strategy against other_strategy.

    >>> beat_two_strat = lambda n: best(n, two_strat)
    >>> winner(20, beat_two_strat, two_strat)
    1
    >>> winner(19, beat_two_strat, two_strat)
    0
    >>> winner(15, beat_two_strat, two_strat)
    0
    >>> winner(0, beat_two_strat, two_strat)
    0
    """
    plan = lambda future_n: best(future_n, other_strategy)
    for choice in range(1, 4):
        if play(plan, other_strategy, n + choice, 1) == 0:
            return choice
    return 1

perfect = lambda n: best(n, perfect)
