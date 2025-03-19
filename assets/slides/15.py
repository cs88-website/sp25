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


def length(s):
    """Return the number of elements in linked list s.

    >>> length(Link(3, Link(4, Link(5))))
    3
    """
    if s is Link.empty:
        return 0
    else:
        return 1 + length(s.rest)

def length_iter(s):
    """Return the number of elements in linked list s.

    >>> length_iter(Link(3, Link(4, Link(5))))
    3
    """
    k = 0
    while s is not Link.empty:
        s, k = s.rest, k + 1
    return k

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
