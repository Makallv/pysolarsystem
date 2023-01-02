"""
Main file for solar system
"""
from Solar_System.SolarSystem import SolarSystem, Sun, Planet
from DrawTurtle import draw


def main():
    """
    Main function for solar system
    """
    # Name the solar system and planets in it
    sun = Sun()
    planets = []
    solar_system = SolarSystem("Milky Way", sun, planets)
    mercury = Planet("Mercury", 579_000, 24.4, "gray")
    venus = Planet("Venus", 672_000, 60.5, "yellowish")
    earth = Planet("Earth", 93_000_000, 63.7, "blue")
    mars = Planet("Mars", 141_000_000, 33.9, "red")
    jupiter = Planet("Jupiter", 483_600_000,  699.1, "orange")
    saturn = Planet("Saturn", 890_700_000, 58.2, "pale yellow")
    uranus = Planet("Uranus", 1_784_000_000, 25.4, "pale blue")
    neptune = Planet("Neptune", 2_793_000_000, 24.6, "pale blue")
    pluto = Planet("Pluto", 3_596_000_000, 11.5, "brown")

    # Add planets to solar system
    solar_system.add_planet(mars)
    solar_system.add_planet(venus)
    solar_system.add_planet(jupiter)
    solar_system.add_planet(saturn)
    solar_system.add_planet(uranus)
    solar_system.add_planet(pluto)
    solar_system.add_planet(mercury)
    solar_system.add_planet(neptune)
    solar_system.add_planet(earth)

    # Print the solar system and it's planets
    solar_system.print_planets()

    # From DrawTurtle file call draw function
    draw()


if __name__ == '__main__':
    """
    Check if is launched as a script or imported module
    """
    main()

