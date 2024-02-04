import bt_sql as db
from fuzzywuzzy import fuzz
import random
from pygame import mixer

class Game():
    def __init__(self, arg = 0, ch =""):
        self.score = 0
        self.song_to_play = 10
        self.list_song = []
        self.fill_list(arg, ch)
        self.current_song = self.rand_song()
        self.clip = "./song/" + self.current_song[1] + ".wav"
        self.player(self.clip)


    def fill_list(self, arg = 0, ch=""):
        '''
        Input : Optionnal.
            arg : int (define a category on which the blind test is processed)
                default 0 -> ALL
                        1 -> date > ch
                        2 -> type = ch
            ch : string (search criteria)
                MUST BE COMPLETED IF arg != 0
        Output : None

        Fill 'list_song' with a list 3-tuple from the db : 
            [(idSong, author, name), ..].
        '''
        if arg == 0:
            ls = db.getAll()
        elif arg == 1:
            ls = db.getDateOverd(ch)
        elif arg == 2:
            ls = db.getType(ch)
        for item in ls:
            self.list_song.append((item[0], item[1], item[2]))

    def rand_song(self):
        '''
        Input : None
        Output : (r1, r2) Current Song - Tuple

        Shuffle the list - Get the first element to return - Delete first element from the list.
        '''
        random.shuffle(self.list_song)
        r = self.list_song[0]
        self.list_song.pop(0)
        return (r[1], r[2])

    def try_test(self, str_author, str_song):
        '''
        Input : str_song : string (The name of the song : User proposal)
        Output : str_author : string (The name of the author : User proposal)

        Increase score if author and/or name are correct
        '''
        if fuzz.token_sort_ratio(str_author, self.current_song[0]) >= 80:
            self.score = self.score + 1
        if fuzz.token_sort_ratio(str_song, self.current_song[1]) >= 80:
            self.score = self.score + 1

        return self.score

    def next(self):
        '''
        Input : None
        Output : None 
        
        Select the next song to play, update the list of song consequently
        '''
        if self.song_to_play == 0 or not self.list_song:
            return
        self.song_to_play = self.song_to_play - 1
        r = self.list_song[0]
        self.list_song.pop(0)
        self.current_song = (r[1], r[2])
        self.clip = "./song/" + self.current_song[1] + ".wav"
        self.player(self.clip)

    def player(self, song):
        mixer.init()
        mixer.music.load(self.clip)
        mixer.music.play()
