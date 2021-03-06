"""
This module holds the Movie structure used to generate the webpage.
"""
import webbrowser


class Movie:
    def __init__(self,
                 title,
                 director,
                 release_date,
                 storyline,
                 poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.director = director
        self.release_date = release_date
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """
        Opens Movie's youtube trailer in a new tab using default browser
        """
        webbrowser.open(self.trailer_youtube_url)