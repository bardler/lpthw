#example class
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "Bum ba dum da daaa da"
                  "This song kind of sucks"])

bulls_on_parade = Song(["They rally around the family",
                        "With a pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()