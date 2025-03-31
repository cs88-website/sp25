
class Link:
    """A linked list.

    >>> Link(1, Link(2, Link(3)))
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> s
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(s)
    <1 <2 3> 4>
    """

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

class Song:
    def __init__(self, name, artist, length):
        """
        >>> all_too_well = Song('All Too Well', 'Taylor Swift', )
        >>> all_too_well.name
        'All Too Well'
        """
        self.name = name
        self.artist = artist
        self.length = length

    def timing(self):
        return f"{self.length // 60}:{self.length % 60}"

    def __repr__(self):
        return f'{self.name} @ {self.timing()}' # skipping artist for now..

def secs_to_timing(s):
    return f"{s // 60}:{s % 60}"

# Thanks to Claude for saving me some typing...
# I should have verified the length but didn't... -mb
fearless = Song("Fearless", "Taylor Swift", 241)
fifteen = Song("Fifteen", "Taylor Swift", 294)
love_story = Song("Love Story", "Taylor Swift", 235)
hey_stephen = Song("Hey Stephen", "Taylor Swift", 254)
white_horse = Song("White Horse", "Taylor Swift", 234)
you_belong_with_me = Song("You Belong With Me", "Taylor Swift", 231)
breathe = Song("Breathe (feat. Colbie Caillat)", "Taylor Swift", 263)
tell_me_why = Song("Tell Me Why", "Taylor Swift", 200)
youre_not_sorry = Song("You're Not Sorry", "Taylor Swift", 261)
the_way_i_loved_you = Song("The Way I Loved You", "Taylor Swift", 244)
forever_and_always = Song("Forever & Always", "Taylor Swift", 225)
the_best_day = Song("The Best Day", "Taylor Swift", 245)
change = Song("Change", "Taylor Swift", 280)

fearless_album = Link(fearless,
                 Link(fifteen,
                 Link(love_story,
                 Link(hey_stephen,
                 Link(white_horse,
                 Link(you_belong_with_me,
                 Link(breathe,
                 Link(tell_me_why,
                 Link(youre_not_sorry,
                 Link(the_way_i_loved_you,
                 Link(forever_and_always,
                 Link(the_best_day,
                 Link(change)))))))))))))

# Recursive function to calculate total album length
def total_album_length(album):
    if album == Link.empty:
        return 0

    # Add current song length to the total length of the rest
    return album.first.length + total_album_length(album.rest)

def longest_song(album):
    if album == Link.empty:
        return None
    if album.rest == Link.empty:
        return album.first

    rest_longest = longest_song(album.rest)
    if album.first.length > rest_longest.length:
        return album.first
    else:
        return rest_longest

def nested_link():
    """
    >>> s = Link(2, Link(3, Link(    4     , Link(5))))
    >>> t = Link(2, Link(3, Link(  Link(4) , Link(5))))
    >>> print(s)
    <2 3 4 5>
    >>> print(t)
    <2 3 <4> 5>
    >>> s = Link(Link(8), Link(Link(4, Link(6, Link(Link(7)))), Link(5)))
    >>> print(s)
    <<8> <4 6 <7>> 5>
    >>> s.first.first
    8
    >>> s.rest.first.rest.rest.first
    Link(7)
    >>> s.rest.first.rest.rest.first.first
    7
    """


#### Bank Accounts

class BaseAccount:
    """Create named accounts with a balance that is
    - increased by account_deposit
    - decreased by account_withdrawl
    """

    # Constructor
    def __init__(self, name, initial_deposit=0, account_number=0, bank=None):
        # Initialize the instance attributes
        self._name = name
        self._bank = bank
        self._acct_no = account_number
        self._balance = initial_deposit

    # Selectors
    def account_name(self):
        return self._name

    def account_balance(self):
        return self._balance

    def account_number(self):
        return self._acct_no

    # Operations
    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance

    def account_type(self):
        return "Base"

    # Display representation
    def __repr__(self):
        return f'<{self.account_type()}Account: {self.account_name()}-{self.account_number()}>'

    # Print representation
    def __str__(self):
        return f'{self.account_type()}Account: {self.account_name()}-{self.account_number()} Balance: {self._balance}'

    # This is only useful for debugging.
    def show_superclass(self):
        return super()

class CheckingAccount(BaseAccount):

    def __init__(self, name, initial_deposit, account_number=0, bank=None):
        # Use superclass initializer
        # BaseAccount.__init__(self, name, initial_deposit, account_number, bank)
        # Alternatively, recommended:
        super().__init__(name, initial_deposit, account_number, bank)
        # Additional initialization

    def withdraw(self, amount):
        """
        Adapt the withdraw methods to prevent "overdrafting"
        """
        if self.account_balance() - amount < 0:
            return "ERROR: You are not allowed to overdraft a CheckingAccount."
        return super().withdraw(amount)

    def account_type(self):
        return "Checking"

    # Just for debugging / example:
    def show_superclass(self):
        return super()

class SavingsAccount(BaseAccount):
    interest_rate = 0.02

    def __init__(self, name, initial_deposit, account_number=0, bank=None):
        # Use superclass initializer
        super().__init__(name, initial_deposit, account_number, bank)

    def accrue_interest(self):
        # We should use `self.interest_rate` so the RetirementSavingsAccount works
        self._balance = self._balance * (1 + self.interest_rate)

    def account_type(self):
        return "Savings"

    # Display representation
    def __repr__(self):
        # Alternatively, we can use `type(self)` to infer the class.
        return f'<{self.account_type()}Account: {self.account_name()}-{self.account_number()} @ {type(self).interest_rate * 100}%>'

class Bank:
    def __init__(self, name, initial_account_number=1000):
        self.name = name
        self.__next_account_no = initial_account_number
        self.__accounts = []

    def new_account(self, name, initial_deposit=0, account_type=CheckingAccount):
        account_no = self.__next_account_no
        account = account_type(name, initial_deposit, account_no, self)
        self.__next_account_no += 1
        self.__accounts.append(account)
        return account

    def show_accounts(self):
        for acct in self.__accounts:
            print(acct)

    def all_accounts(self):
        return tuple(self.__accounts)

    # This allows us to write len(bank)
    def __len__(self):
        return len(self.__accounts)

    def total_assets(self):
        return sum(map(lambda a: a.account_balance(), self.__accounts))

    def __str__(self):
        return f"Bank of {self.name} with {len(self)} accounts."

    def account_types():
        return {
            'Checking': CheckingAccount,
            'Savings': SavingsAccount,
            'RetirementSavings': RetirementSavingsAccount
        }

#berkeley = Bank('UC Berkeley')
#cs88 = berkeley.new_account('CS88', 1000, CheckingAccount)
#cs61a = berkeley.new_account('CS61A', 1, SavingsAccount)

#berkeley.new_account('CS88 Retirement', 1000, RetirementSavingsAccount)

# Now we can find an account:
#retirement = berkeley.all_accounts()[-1]

# What kinds of accounts exist in our bank?
#Bank.account_types()
