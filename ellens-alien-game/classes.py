"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0

    def __init__(self, x_co, y_co) -> None:
        Alien.total_aliens_created += 1
        self.x_coordinate = x_co
        self.y_coordinate = y_co
        self.health = 3

    def hit(self):
        """To track the health"""
        self.health -= 1

    def is_alive(self):
        """Check if alive"""
        if self.health > 0:
            return True
        return False

    def teleport(self, x_co, y_co):
        """Check if teleport for """
        self.x_coordinate = x_co
        self.y_coordinate = y_co

    def collision_detection(self, co_ordinates):
        pass



def new_aliens_collection(alein_start_positions):
    """New aliens created collection"""
    alien_objs = []
    for alien in alein_start_positions:
        alien_objs.append(Alien(alien[0], alien[1]))
    return alien_objs
