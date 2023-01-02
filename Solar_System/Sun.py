
class Star:
    """A class representing a star.

    Attributes:
        name (str): The name of the star.
        mass (float): The mass of the star in kilograms.
    """

    def __init__(self, name: str, mass: float):
        self.name = name
        self.mass = mass


class Sun(Star):
    """A class representing the sun.

    Inherits from the Star class.

    Attributes:
        name NOQA (str): The name of the sun (default "Sun").
        mass NOQA (float): The mass of the sun in kilograms (default 1.989 x 10^30).
    """

    def __init__(self, name: str = "Sun", mass: float = 1.989 * 10 ** 30):
        super().__init__(name, mass)
