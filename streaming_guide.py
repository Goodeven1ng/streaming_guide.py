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
    """Represents a streaming service, holding a catalog (dict) of Movie objects."""

    def __init__(self, name):
        """Initialize a new StreamingService.

        Args:
            name (str): The name of the streaming service.
        """
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Return the name of the streaming service."""
        return self._name

    def get_catalog(self):
        """Return the entire catalog (a dict mapping title→Movie)."""
        return self._catalog

    def add_movie(self, movie):
        """Add a Movie object to this service's catalog.

        Args:
            movie (Movie): The Movie instance to add.
        """
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, title):
        """Remove a movie from the catalog by its title.

        Args:
            title (str): The title of the movie to remove.
        """
        if title in self._catalog:
            del self._catalog[title]


class StreamingGuide:
    """Manages multiple StreamingService instances to answer 'where_to_watch' queries."""

    def __init__(self):
        """Initialize a new StreamingGuide with an empty list of services."""
        self._streaming_services = []

    def add_streaming_service(self, service):
        """Add a StreamingService to this guide.

        Args:
            service (StreamingService): The service to add.
        """
        self._streaming_services.append(service)

    def delete_streaming_service(self, name):
        """Remove a StreamingService (by name) from this guide.

        Args:
            name (str): The name of the service to remove.
        """
        self._streaming_services = [
            svc for svc in self._streaming_services 
            if svc.get_name() != name
        ]

    def where_to_watch(self, title):
        """Return a list whose first element is "Title (Year)", followed by service names.

        Args:
            title (str): The movie title to search for.

        Returns:
            list or None: List with first element as "Title (Year)" followed by service names,
                         or None if movie not found
        """
        found_year = None
        services_with_movie = []
        
        # Find the movie and collect services that have it
        for service in self._streaming_services:
            if title in service.get_catalog():
                movie = service.get_catalog()[title]
                if found_year is None:  # Only need to get the year once
                    found_year = movie.get_year()
                services_with_movie.append(service.get_name())
        
        if found_year is None:
            return None
        
        # Format the result as ["Title (Year)", "Service1", "Service2", ...]
        return [f"{title} ({found_year})"] + services_with_movie
