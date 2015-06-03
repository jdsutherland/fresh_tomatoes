import webbrowser


class Movie:
    def __init__(self, title, director, release_date, storyline, poster_img, youtube_trailer_url):
        self.title = title
        self.director = director
        self.release_date = release_date
        self.storyline = storyline
        self.poster_img = poster_img
        self.youtube_trailer_url = youtube_trailer_url

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)
