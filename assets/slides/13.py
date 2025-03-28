class Flower:
    bee_visits = {}
    all_flowers = []

    def __init__(self, name, num_petals, color):
        self.name = name
        self.num_petals = num_petals
        self.color = color
        # next two lines are the same.
        # Flower.all_flowers.append(self)
        print(f'before: all flowers: {self.all_flowers}')
        self.all_flowers.append(self)
        print(f'after: all flowers: {self.all_flowers}')
        # self.bee_visits = []

    def describe(self):
        print(f"The {self.name} is {self.color} and has {self.num_petals} petals.")

    def __str__(self):
        return self.describe()

    def add_visit(self, bee_name):
        """A tweak to the midterm question....
        >>> rose = Flower("rose", 30, "blue")
        >>> daisy = Flower("daisy", 56, "yellow")

        >>> rose.add_visit("lucky bee")
        >>> daisy.add_visit("small bee")
        >>> rose.add_visit("cute bee")
        >>> daisy.add_visit("happy bee")
        >>> rose.add_visit("lucky bee")
        """
        if self.name not in self.bee_visits:
            self.bee_visits[self.name] = []
        if bee_name not in self.bee_visits[self.name]:
            self.bee_visits[self.name].append(bee_name)

def demos():
    """Demos.

    >>> b = Account('Ada')
    >>> f = b.deposit
    >>> f(5)
    5
    >>> f(25)
    30
    >>> b.balance
    30
    >>> a = Account('Alan')
    >>> [a.deposit(n) for n in range(10)]
    [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    >>> m = map(a.deposit, range(10, 13))
    >>> next(m)
    55
    >>> a.balance
    55
    >>> next(m)
    66
    >>> next(m)
    78
    >>> a.balance
    78
    >>> d = {1: 10, 2: 5, 3: 15, 4: 8, 5: 4}
    >>> max(d.keys(), key=d.get)
    3
    """

class Clown:
    """An illustration of a class statement. This class is not useful.

    >>> Clown.nose
    'big and red'
    >>> Clown.dance()
    'No thanks'
    """
    nose = 'big and red'
    def dance():
        return 'No thanks'

class Town:
    """Waldo in town.

    >>> Town(1, 7).street[2]
    'Waldo'
    """
    def __init__(self, w, aldo):
        if aldo == 7:
            self.street = {self.f(w): 'Waldo'}

    def f(self, x):
        return x + 1


class Beach:
    """Waldo at the beach.

    >>> Beach().walk(0).wave(0)
    'Waldo'
    """
    def __init__(self):
        sand = ['Wal', 'do']
        self.dig = sand.pop

    def walk(self, x):
        self.wave = lambda y: self.dig(x) + self.dig(y)
        return self


# a = Account('C88C')
# b = Account('CS61A')
# c = Account('CS61B')

class Account:
    """An account has a balance and a holder.
    All accounts share a common interest rate.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> Account.interest
    0.02
    """
    interest = 0.02
    all_accounts = []

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
        self.all_accounts.append(self)
        # Account.all_accounts.append(self)
        # all_accounts.append(self)

    def inspect_interest(self):
        print(f'Self.interest is {self.interest} --- Account.interest is {Account.interest}')

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
