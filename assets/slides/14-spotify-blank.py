### DEMO: DESIGN SPOTIFY (BLANK VERSION) ###

class User:
    def __init__(self, name):
        """
        >>> rebecca = User('Rebecca')
        >>> rebecca.name
        'Rebecca'
        >>> rebecca.playlists
        []
        """
        pass

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
        pass

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
        pass

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
        pass

    def play(self):
        pass

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
        pass
