class Movie():
    """ This is a Movie class containing basic information,
    such as the title, storyline, poster image's URL,
    and YouTube URL of the trailer for the movie.

    Arguments:
    title (str): This is the title of the movie.
    storyline (str): A short summary of the movie.
    poster_image_url (str): A URL of an image file for the movie.
    trailer_youtube_url (str): Youtube URL of the movie's trailer.

    """

    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
