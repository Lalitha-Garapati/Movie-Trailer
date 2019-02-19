import webbrowser

class Movie():
    def __init__(self, movie_title, movie_language, movie_storyline, poster_image, trailer_youtube_video):
        self.title = movie_title
        self.language = movie_language
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_video

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
