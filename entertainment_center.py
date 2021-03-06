"""
This module acts as the driver for the application.
A static list of favorite movies is instantiated and the
fresh_tomatoes module is used to generate the webpage.
"""
import fresh_tomatoes
import media


def instantiate_movies():
    """ Returns list of favorite movies """

    ex_machina = media.Movie(
        "Ex Machina",
        "Alex Garland",
        "January 21 2015",
        "A young programmer is selected to participate in AI study by company founder.",
        "http://ia.media-imdb.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SX214_AL_.jpg",
        "https://youtu.be/gyKqHOgMi4g")

    goodfellas = media.Movie(
        "GoodFellas",
        "Martin Scorsese",
        "September 19 1990",
        "Henry Hill and his friends work their way through the mob hierarchy.",
        "http://ia.media-imdb.com/images/M/MV5BMTY2OTE5MzQ3MV5BMl5BanBnXkFtZTgwMTY2NTYxMTE@._V1_SX214_AL_.jpg",
        "https://youtu.be/qo5jJpHtI1Y")

    saving_private_ryan = media.Movie(
        "Saving Private Ryan",
        "Steven Spielberg",
        "July 24 1998",
        "During WW2, a group of U.S. soldiers rescue a paratrooper whose brothers have all been KIA.",
        "http://upload.wikimedia.org/wikipedia/en/thumb/a/ac/Saving_Private_Ryan_poster.jpg/220px-Saving_Private_Ryan_poster.jpg",
        "https://youtu.be/zwhP5b4tD6g")

    superbad = media.Movie(
        "Superbad",
        "Greg Mottola",
        "August 17 2007",
        "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage \
        a booze-soaked party goes awry.",
        "http://upload.wikimedia.org/wikipedia/en/thumb/8/8b/Superbad_Poster.png/220px-Superbad_Poster.png",
        "https://youtu.be/4q5Mi9gWX8c")

    troll2 = media.Movie(
        "Troll 2",
        "Claudio Fragasso",
        "October 12 1990",
        "Comedy gold",
        "http://upload.wikimedia.org/wikipedia/en/9/9e/Troll_2_poster.jpg",
        "https://youtu.be/GO6JVBygYxQ")

    office_space = media.Movie(
        "Office Space",
        "Mike Judge",
        "February 19 1999",
        "Three software devs hate their jobs and decide to rebel against their greedy boss.",
        "http://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Office_space_poster.jpg/220px-Office_space_poster.jpg",
        "https://youtu.be/_IwzZYRejZQ")

    return [ex_machina,
            goodfellas,
            saving_private_ryan,
            superbad,
            troll2,
            office_space]


def main():
    """
    Main entry point of Fresh Tomatoes app
    """
    movies = instantiate_movies()

    # generate html and load the page
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()