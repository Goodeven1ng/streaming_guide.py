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


class StreamingService:
    """Represents a streaming service, holding a collection of Movie objects."""

    def __init__(self, name):
        """Initialize a new StreamingService.

        Args:
            name (str): The name of the streaming service.
        """
        self._name = name
        self._movies = []

    def get_name(self):
        """Return the name of the streaming service."""
        return self._name

    def get_movies(self):
        """Return a list of all Movie objects currently in this service's catalog."""
        return list(self._movies)

    def add_movie(self, movie):
        """Add a Movie object to this streaming service's catalog.

        Args:
            movie (Movie): The Movie instance to add.
        """
        self._movies.append(movie)

    def delete_movie(self, title):
        """Delete a movie from the catalog by matching its title.

        Args:
            title (str): The title of the movie to remove.
        """
        for idx, m in enumerate(self._movies):
            if m.get_title() == title:
                self._movies.pop(idx)
                break


class StreamingGuide:
    """Manages multiple StreamingService instances to answer 'where to watch' queries."""

    def __init__(self):
        """Initialize a new StreamingGuide with no services."""
        self._services = []

    def add_streaming_service(self, service):
        """Add a StreamingService to this guide.

        Args:
            service (StreamingService): The service to add.
        """
        self._services.append(service)

    def delete_streaming_service(self, name):
        """Remove a streaming service by name.

        Args:
            name (str): The name of the service to remove.
        """
        for idx, svc in enumerate(self._services):
            if svc.get_name() == name:
                self._services.pop(idx)
                break

    def where_to_watch(self, title):
        """Return a list of service names that currently offer a movie with the given title.

        Args:
            title (str): The movie title to search for.

        Returns:
            List[str]: Names of services whose catalog includes a Movie with this title.
        """
        available_on = []
        for svc in self._services:
            for movie in svc.get_movies():
                if movie.get_title() == title:
                    available_on.append(svc.get_name())
                    break
        return available_on
