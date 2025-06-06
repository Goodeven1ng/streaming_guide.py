# Assignment_10
# Author_Mutaz_Al_-_Shara
# Instructor_Rita_M_Ghantous
# Date_June_6th_2025
# Engr_103_401_S2025
# Streaming_Guide.Py

"""
Module for managing streaming services and their movie catalogs.
Includes classes for Movie, StreamingService and StreamingGuide.
"""


class Movie:
    """Represents a movie with title, genre, director, and year."""

    def __init__(self, title, genre, director, year):
        """Initialize a new Movie instance.

        Args:
            title (str): The title of the movie
            genre (str): The genre of the movie
            director (str): The director of the movie
            year (int): The release year of the movie
        """
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """Return the movie title."""
        return self._title

    def get_genre(self):
        """Return the movie genre."""
        return self._genre

    def get_director(self):
        """Return the movie director."""
        return self._director

    def get_year(self):
        """Return the movie release year."""
        return self._year