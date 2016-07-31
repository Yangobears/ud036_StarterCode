class Movie:
    """This class is the representation of a movie object"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Args: 
          title(str): movie title
          poster_image_url(str): image of the movie poster
          trailer_youtube_url(str): link to youtube video of the trailer of the movie

        """

        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
