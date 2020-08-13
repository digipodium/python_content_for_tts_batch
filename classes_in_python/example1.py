class Movie:

    def __init__(self,title, year, director, cast=[], summary=""):
        self.title = title
        self.year = year
        self.director = director
        self.cast= cast
        self.summary = summary

    def view_details(self):
        print("Movie data:")
        print(self.title)
        print(self.director)
        print(self.year)
        print(self.cast)
        print(self.summary)

    def update_cast(self, member):
        print(f"added {member} to movie cast")
        self.cast.append(member)

    def get_movie_age(self):
        return 2020 - self.age
    
    def __repr__(self):
        return f"{self.title} ({self.year})"