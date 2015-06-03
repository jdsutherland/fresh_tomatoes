import fresh_tomatoes
import media

# TODO: docstring
def instantiate_movies():
    ex_machina = media.Movie("Ex Machina",
        "Alex Garland", 
        "1/21/2015", 
        "Young programmer selected to participate in AI study by company founder.",
        "http://ia.media-imdb.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SX214_AL_.jpg",
        "https://youtu.be/gyKqHOgMi4g")

    goodfellas = media.Movie("GoodFellas",
        "Martin Scorsese",
        "9/19/1990",
        "Henry Hill and his friends work their way through the mob hierarchy.",
        "http://ia.media-imdb.com/images/M/MV5BMTY2OTE5MzQ3MV5BMl5BanBnXkFtZTgwMTY2NTYxMTE@._V1_SX214_AL_.jpg",
        "https://youtu.be/qo5jJpHtI1Y")
        
    superbad = media.Movie("Superbad",
        "Greg Mottola",
        "8/17/2007",
        "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.",
        "http://ia.media-imdb.com/images/M/MV5BMTc0NjIyMjA2OF5BMl5BanBnXkFtZTcwMzIxNDE1MQ@@._V1_SX214_AL_.jpg",
        "https://youtu.be/4q5Mi9gWX8c")

    return [ex_machina, goodfellas, superbad]


def main():
  movies = instantiate_movies()
  fresh_tomatoes.open_movies_page(movies)

  

if __name__ ==  '__main__':
    main()
