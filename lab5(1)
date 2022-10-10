import datetime
class Human:
    def __init__(self, name, sex, birth_year):
        self.name=name
        self.sex=sex
        self.birth_year=birth_year

human = Human(name = "Alena", sex = "W", birth_year = 2001)
 

class Movie:
    def __init__ (self, name, director, year, country, 
                duration, age_rating  ):
        self.name=name
        self.director=director
        self.year=year
        self.country=country
        self.duration=duration
        self.age_rating=age_rating
        
    def is_allowed(self, Human):
        now = datetime.datetime.now()
        current_year = now.year
        flag = True
        if(current_year - Human.birth_year <= self.age_rating):
                flag = False
        return flag        

                

movie = Movie(name = "Dune", director = "Denis Villeneuve", 
              year = 2021, country = "USA", duration = 155, 
              age_rating = 13)

print(movie.is_allowed(human))



class Cartoon(Movie):
    def __init__(self, technique, name, director, year, country, 
                duration, age_rating):
        Movie.__init__(self, name, director, year, country, 
                duration, age_rating)
        self.technique = technique
        
cartoon = Cartoon(name = "Treasure Island", director = "David Cherkasskiy", 
              year = 1971, country = "USSR", duration = 107, 
              age_rating = 6, technique = "Multiplication")  

class Anime(Cartoon):
    def __init__(self, technique, name, director, year, country, 
                duration, age_rating):
        Cartoon.__init__(self,technique, name, director, year,  country,
                duration, age_rating)
        self.country = "Japan"
        self.tehnique = "SUPER_ANIME_TECHNIQUE"
        
anime = Anime(name = "Cyberpunk: Edgerunners", director = "Hirouki Imaisi", 
              year = 2022, country = "Japan", duration = 24, 
              age_rating = 18, technique = "2d_mutiplication")
