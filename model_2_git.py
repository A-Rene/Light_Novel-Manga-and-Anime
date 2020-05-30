# Model Light novels, Manga, Anime 
class LightNovel:
    """A light novel model  """
    def __init__(self, series_name, author, publisher=None):
        """Initialize the attributes"""
        self.series = series_name
        self.book = ''
        self.author = author
        self.publisher = publisher
        self.sysnopsis = None
        self.illistrator = None
        self.volume = None
        

    def book_name(self, book):
        """Book name in the series """
        self.book = book
        return self.book


    def author_name(self):
        """Print only the author name"""
        print(f"{self.author}")



    def more_than_one_author(self):
        """If there is more than one aouthor split the names apart """
        if ',' in self.author:
            self.author = self.author.split(',')
            return self.author


    def one_sentence_sysnopsis(self, sysnopsis):
        """Give one sentence sysnopsis of the story """
        self.sysnopsis = sysnopsis
        return self.sysnopsis


    def light_novel_illistrator(self, illistrator_LN):
        """Name of light novel illistrator"""
        self.illistrator = illistrator_LN
        return self.illistrator

    
    def set_volume(self, number):
        """Number of episodes in the anime series"""
        self.volume = number 
        return self.volume 


    def full_description(self):
        """Print out a full discription"""
    # if there is a publisher include that in the description 
        if self.publisher:
             lightnovel = {'Light Novel Series Name': self.series,
                            'Book Name' : self.book,
                            'Publisher' : self.publisher,
                            'Author' :  self.author,
                            'Illistrator' : self.illistrator,
                            'Volume Number' : self.volume ,
                            'Synopsis' :  self.sysnopsis,

                        }
        else:
            lightnovel = {'Light Novel Series Name': self.series,
                            'Book Name' : self.book,
                            'Author' :  self.author,
                            'Illistrator' : self.illistrator,
                            'Volume Number' : self.volume ,
                            'Synopsis' :  self.sysnopsis,
                        }
        for key, value in lightnovel.items():
            print(f"{key} : {value}")





class Manga(LightNovel):
    """A manga model"""
    def __init__(self, series_name, author, publisher=None):
        """Inherit Light novel attributs and add what I need"""
        super().__init__(series_name, author, publisher)
        self.artist = None
        

    def manga_artist(self, artist_name):
        """The name of the manga artist for the particular instance """
        print(f"Manga Artist: {artist_name} ")
        self.artist = artist_name
        return self.artist

    def full_description(self):
        """Print out a full discription"""
    # if there is a publisher include that in the description 
        if self.publisher:
             manga = {'Manga Series' : self.series,
                'Publisher' : self.publisher, 
                'Author' : self.author, 
                'Manga Artist' :  self.artist,
                'Volume Number' : self.volume ,
                'Synopsis'  : self.sysnopsis

                }
        else:
            manga = {'Manga Series': self.series,
                        'Publisher' : self.publisher,
                        'Author' :  self.author,
                        'Manga Artist' : self.artist,
                        'Volume Number' : self.volume ,
                        'Synopsis' :  self.sysnopsis,
                        }
        for key, value in manga.items():
            print(f"{key} : {value}")





class Anime: 
    """ An anime model"""
    def __init__(self, anime_name, animation_studio): 
        """Initialize attribute values """
        self.anime = anime_name
        self.studio = animation_studio
        self.voice_actors = ''
        self.composer = None
        self.episode_num = None
        self.lead_character = None
        self.characters = ''
        self.director = None 
        self.producer = ''
        self.sysnopsis = None


    def character_voice(self, voice):
        """The voice actors for the notable characters """
        if self.voice_actors == '':
            self.voice_actors = f"{voice}"
        else:
            self.voice_actors += f", {voice}"
        return self.voice_actors



    def anime_characters(self, show_character):
        """The voice actors for the notable characters """
        if self.characters == '':
            self.characters = f"{show_character}"
        else:
            self.characters += f", {show_character}"
        return self.characters


    def main_character(self, main):
        """Return the name of the main character"""
        self.lead_character = main
        return self.lead_character



    def set_episode_number(self, number):
        """Number of episodes in the anime series"""
        self.episode_num = number 
        return self.episode_num


    def music_composer(self, composer): 
        """Score composer of the soundtraks """
        self.composer = composer
        return self.composer


    def animation_director(self, director):
        """Animation director"""
        self.director = director


    def show_producer(self, producer):
        """Names of show producers"""
        if self.producer == '':
            self.producer = f"{producer}"
        else:
            self.producer += f", {producer}"
        return self.producer



    def one_sentence_sysnopsis(self, sysnopsis):
        """Give one sentence sysnopsis of the story """
        self.sysnopsis = sysnopsis
        return self.sysnopsis



    def anime_desciption(self):
        """Make a dictionary out of the information """
        anime = {
                'Anime' : self.anime,
                'Animation Studio' : self.studio,
                'Voice Actors' : self.voice_actors.split(','),
                'Lead Character' : self.lead_character,
                'Characters' : self.characters.split(','),
                'Director' : self.director,
                'Show Producer' : self.producer.split(','),
                'Episode Number' : self.episode_num,
                'Soundtrack Composer' : self.composer,
                'Synopsis' : self.sysnopsis,

                }
        for key, value in anime.items():
            print(f"{key} : {value}")

