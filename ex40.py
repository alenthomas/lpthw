class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
# adds happy_bday as an object of Song 
# also Song take a list of strings
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
#added comment
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

thing = Song("hai")
thing.sing_me_a_song()

thing.sing_me_a_song()
