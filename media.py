import webbrowser


class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    __doc__ = """Movie class

    __init__ -- Constructor method initializes given parameters
    show_trailer -- Opens a link to the youtube trailer property 
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
