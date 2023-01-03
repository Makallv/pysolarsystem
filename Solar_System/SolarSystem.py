"""
Class solar system
"""

from Solar_System.Sun import Sun
from Solar_System.Planet import Planet


class SolarSystem:
    """
    A class representing a solar system.

       Attributes:
           name (str): The name of the solar system.
           sun (Sun): The sun in the solar system.
           planets (List[Planet]): A list of planets in the solar system.
       """

    def __init__(self, name: str, sun: Sun, planets: list[Planet]):
        self.name = name
        self.sun = sun
        self.planets = planets

    def add_planet(self, planet: Planet):
        """
        Add a planet to the solar system.

        Args:
            planet (Planet): The planet to add to the solar system.
        """
        self.planets.append(planet)

    def sort_planets(self):
        """
        Sort the list of planets in the solar system by their distance to the sun, from furthest to closest.
        """
        self.planets.sort(key=lambda planet: planet.distance_to_sun, reverse=True)

    def print_planets(self):
        """
        Print the list of planets in the solar system, including the sun.
        """
        print(f"{self.name}'s galaxy:")
        print(f"{self.sun.name}: {self.sun.mass:,.0f} kg")
        print("Unsorted list:")
        for planet in self.planets:
            print(f"{planet.name}: {planet.distance_to_sun:,.0f} km")
        self.sort_planets()
        print("\nSorted list: (From furthest from the sun to the closest)")
        for planet in self.planets:
            print(f"{planet.name}: {planet.distance_to_sun:,.0f} km")


