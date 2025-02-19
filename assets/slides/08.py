all_but_first = lambda word: word[1:]
all_but_last = lambda word: word[:-1]

def palindrome(word):
    """
    >>> palindrome('c88c')
    True
    >>> palindrome('cs61a')
    False
    >>> palindrome('racecar')
    False
    >>> palindrome('lol')
    True
    """
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return palindrome(all_but_first(all_but_last(word)))
    return False

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m

# count_partitions(5, 3)

def fib(n):
    """
    >>> fib(5)
    5
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# if n < 2:
#     return n
# else:
#     return fib(n - 1) + fib(n - 2)

def iter_fib(n):
    """
    >>> iter_fib(5)
    5
    """
    (n_1, n_2) = (0, 1)
    for i in range(0, n):
        # This computes n_1+n_2 before updating n_1
        (n_1, n_2) = (n_2, n_1 + n_2)
    return n_1

def count_change(value, coins):
    """Returns the number of ways to make change for amount.

    >>> denominations = [50, 25, 10, 5, 1]
    >>> count_change(7, denominations)
    2
    >>> count_change(100, denominations)
    292
    >>> denominations = [16, 8, 4, 2, 1]
    >>> count_change(7, denominations)
    6
    >>> count_change(10, denominations)
    14
    >>> count_change(20, denominations)
    60
    """
    if value < 0 or len(coins) == 0:
        return 0
    elif value == 0:
        return 1
    using_coin = count_change(value - coins[0], coins)
    not_using_coin = count_change(value, coins[1:])
    return using_coin + not_using_coin




def streak(n):
    """Return whether positive n is a dice integer in which all the digits are the same.

    >>> streak(22222)
    True
    >>> streak(4)
    True
    >>> streak(22322)  # 2 and 3 are different digits.
    False
    >>> streak(99999)  # 9 is not allowed in a dice integer.
    False
    >>> streak(505)
    False
    >>> streak(707)
    False
    >>> streak(7070)
    False
    >>> streak(33333333333333)
    True
    """
    return (n >= 1 and n <= 6) or (n >= 10 and n % 10 == n // 10 % 10 and streak(n // 10))

def smallest_factor(n):
    """Return the smallest divisor of n above 1.

    >>> smallest_factor(10)
    2
    >>> smallest_factor(45)
    3
    >>> smallest_factor(49)
    7
    """
    def smallest_divisor(k):
        "Return the smallest divisor of n above or equal to k."
        if n % k == 0:
            return k
        else:
            return smallest_divisor(k + 1)
    return smallest_divisor(2)

def unique_prime_factors(n):
    """Return the number of unique prime factors of n.

    >>> unique_prime_factors(51)  # 3 * 17
    2
    >>> unique_prime_factors(9)   # 3 * 3
    1
    >>> unique_prime_factors(576) # 2 * 2 * 2 * 2 * 2 * 2 * 3 * 3
    2
    """
    k = smallest_factor(n)
    def no_k(n):
        "Return the number of unique prime factors of n other than k."
        if n == 1:
            return 0
        elif n % k != 0:
            return unique_prime_factors(n)
        else:
            return no_k(n // k)
    return 1 + no_k(n)

def sevens_iter(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens_iter(2, 5)
    2
    >>> sevens_iter(6, 5)
    1
    >>> sevens_iter(7, 5)
    2
    >>> sevens_iter(8, 5)
    1
    >>> sevens_iter(9, 5)
    5
    >>> sevens_iter(18, 5)
    2
    """
    i, who, direction = 1, 1, 1
    while i < n:
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        who = who + direction
        if who > k:
            who = 1
        if who < 1:
            who = k
        i = i + 1
    return who

def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        who = who + direction
        if who > k:
            who = 1
        if who < 1:
            who = k
        return f(i + 1, who, direction)
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)

def count_park(n):
    """Count the ways to park cars and motorcycles in n adjacent spots.
    >>> count_park(1)  # '.' or '%'
    2
    >>> count_park(2)  # '..', '.%', '%.', '%%', or '<>'
    5
    >>> count_park(4)  # some examples: '<><>', '.%%.', '%<>%', '%.<>'
    29
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return 2 * count_park(n-1) + count_park(n-2)

######### Example that's barely functional,
### but conveys the idea of trees.
### ignore all the stuff about dealing with filepaths...

import os, math
def is_file(directory, file_name):
    return os.path.isfile(os.path.join(directory, file_name))

def walk_directory(directory, indent='', max_depth=math.inf):
    """
    This function just prints ALL files and folders, and goes through all subfolders.
    e.g. walk_directory('/Users/Michael/Desktop')
    """
    all_items = os.listdir(directory)
    for item in all_items:
        if is_file(directory,item):
            print(f'{indent}FILE: {item}')
        else:
            print(f'{indent}DIRECTORY: {item}')
            if max_depth > 0:
                walk_directory(os.path.join(directory, item), indent + '\t', max_depth -1)
            else:
                print(f'{indent}\t...max depth reached.')
