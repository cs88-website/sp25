### INHERITANCE BASICS ###

class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print(f'{self.name} made a noise!')

class Dog(Animal):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def make_noise(self):
        print('Woof!')


class Cat(Animal):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def make_noise(self):
        print('Meow!')


### LOOKUP EXERCISE ###

class A:
    foo = 0
    def __init__(self, foo, bar):
        self.foo = foo + A.foo
        A.foo += 1
        self.bar = bar

class B(A):
    foo = 5
    def __init__(self, bar):
        super().__init__(B.foo, bar)


### TYPE VS. ISINSTANCE ###

class C:
    pass

class D(C):
    pass


### DEMO: DESIGN SPOTIFY (SOLUTION) ###

class User:
    def __init__(self, name):
        """
        >>> rebecca = User('Rebecca')
        >>> rebecca.name
        'Rebecca'
        >>> rebecca.playlists
        []
        """
        self.name = name
        self.playlists = []

class Artist(User):
    def __init__(self, name):
        """
        >>> taylor = Artist('Taylor Swift')
        >>> taylor.name
        'Taylor Swift'
        >>> taylor.playlists
        []
        >>> taylor.albums
        []
        """
        super().__init__(name)
        self.albums = []

class Song:
    def __init__(self, name, artist):
        """
        >>> taylor = Artist('Taylor Swift')
        >>> all_too_well = Song('All Too Well', taylor)
        >>> all_too_well.name
        'All Too Well'
        >>> all_too_well.artist.name
        'Taylor Swift'
        """
        self.name = name
        self.artist = artist

class Playlist:
    def __init__(self, name, songs, owner):
        """
        >>> rebecca = User('Rebecca')
        >>> taylor = Artist('Taylor Swift')
        >>> ed = Artist('Ed Sheeran')
        >>> all_too_well = Song('All Too Well', taylor)
        >>> trouble = Song('I Knew You Were Trouble', taylor)
        >>> happier = Song('Happier', ed)
        >>> breakups = Playlist('Breakups', [all_too_well, trouble, happier], rebecca)
        >>> breakups.name
        'Breakups'
        >>> breakups.play()
        All Too Well by Taylor Swift
        I Knew You Were Trouble by Taylor Swift
        Happier by Ed Sheeran
        >>> breakups.owner is rebecca
        True
        >>> len(rebecca.playlists)
        1
        >>> breakups is rebecca.playlists[0]
        True
        """
        self.name = name
        self.songs = songs
        self.owner = owner
        self.owner.playlists.append(self)

    def play(self):
        for song in self.songs:
            print(f'{song.name} by {song.artist.name}')

class Album(Playlist):
    def __init__(self, name, songs, artist):
        """
        >>> taylor = Artist('Taylor Swift')
        >>> all_too_well = Song('All Too Well', taylor)
        >>> trouble = Song('I Knew You Were Trouble', taylor)
        >>> red = Album('Red', [all_too_well, trouble], taylor)
        >>> red.name
        'Red'
        >>> red.owner.name
        'Taylor Swift'
        >>> red.play()
        All Too Well by Taylor Swift
        I Knew You Were Trouble by Taylor Swift
        >>> len(taylor.albums)
        1
        >>> red is taylor.albums[0]
        True
        """
        super().__init__(name, songs, artist)
        self.owner.albums.append(self)


### MULTIPLE INHERITANCE ###

class Grandparent:
    def where_am_i(self):
        print('In grandparent')

class Parent1(Grandparent):
    def where_am_i(self):
        super().where_am_i()
        print('In parent 1')

class Parent2(Grandparent):
    def where_am_i(self):
        super().where_am_i()
        print('In parent 2')

class Child(Parent1, Parent2):
    def where_am_i(self):
        super().where_am_i()
        print('In child')
