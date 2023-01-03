"""
Planet class
"""

import turtle


class Planet:
    """
    Initializer, turtle draw method, planet list and scale

    Argument:
        name (str): The name of the planet.
        distance_to_sun (float): The distance of the planet to the sun in kilometers.
        radius (float): The radius of the planet in kilometers.
        color (str): The color of the planet.
    """

    def __init__(self, name: str, distance_to_sun: int, radius: float, color: str):
        self.name = name
        self.distance_to_sun = distance_to_sun
        self.radius = radius
        self.color = color



