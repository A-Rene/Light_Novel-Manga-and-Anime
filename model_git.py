# Model Light novels, Manga, Anime Goal: gather information about these seperate classes
class LightNovel:
    """A light novel model  """
    def __init__(self, work_name, author, publisher=None):
        """Initialize the attributes"""
        self.work = work_name
        self.author = author
        self.publisher = publisher
        self.sysnopsis = None

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



    def full_description(self):
        """Print out a full discription"""
    # if there is a publisher include that in the description 
        if self.publisher:
             print(f"Light Novel\n{self.work} Published by {self.publisher}: Written by {self.author}"
                f"\nSynopsis: {self.sysnopsis}")
        else:
            print(f"{self.work} written by {self.author}"
                f"\nSynopsis: {self.sysnopsis}")



class Manga(LightNovel):
    """A manga model"""
    def __init__(self, work_name, author, publisher=None):
        """Inherit Light novel attributs and add what I need"""
        super().__init__(work_name, author, publisher)
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
             print(f"Manga\n{self.work} Published by {self.publisher}, Written by "
                f"{self.author}, Illistrated by: {self.artist}"
                f"\nSynopsis: {self.sysnopsis}")
        else:
            print(f"{self.work} written by {self.author} Illistrated by: {self.artist}"
                f"\nSynopsis: {self.sysnopsis}")


class Anime: 
    """ An anime model"""
    def __init__(self, anime_name, animation_studio): 
        """Initialize attribute values """
        self.anime = anime_name
        self.studio = animation_studio
        self.voice_actors = None
        self.composer = None
        self.episode_num = 0
        self.lead_character = None
        self.characters = None
        self.directior = None 


    def character_voice(self, voice):
        """The voice actors for the notable characters """
        if self.voice_actors == None:
            self.voice_actors = f"{voice}"
        else:
            self.voice_actors += f", {voice}"
        return self.voice_actors


    def main_character(self, main):
        """Return the name of the main character"""
        self.lead_character = main
        return self.lead_character


    def description(self):
        """Give a description of the anime """
        print(f"{self.lead_character}, {self.anime} {self.voice_actors}")




