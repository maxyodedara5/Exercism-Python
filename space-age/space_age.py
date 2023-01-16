"""Script for Calculating ages on different planets"""

class SpaceAge:
    """Calculates ages on different planets"""
    def __init__(self, seconds):
        self.seconds_passed = seconds

    def on_earth(self):
        """Age on function planet"""
        return round(self.seconds_passed / 31557600 , 2)

    def on_mercury(self):
        """Age on function planet"""
        return round(self.seconds_passed / (31557600 * 0.2408467) , 2)

    def on_venus(self):
        """Age on function planet"""
        return round(self.seconds_passed / (31557600 * 0.61519726) , 2)

    def on_mars(self):
        """Age on function planet"""
        return round(self.seconds_passed / (31557600 * 1.8808158) , 2)

    def on_jupiter(self):
        """Age on function planet"""
        return round(self.seconds_passed / (31557600 * 11.862615) , 2)

    def on_saturn(self):
        """Age on function planet"""
        return round(self.seconds_passed / (31557600 * 29.447498) , 2)

    def on_uranus(self):
        """Age on function planet"""
        # lol, Uranus !
        return round(self.seconds_passed / (31557600 * 84.016846) , 2)

    def on_neptune(self):
        """Age on function planet"""
        return round(self.seconds_passed / (31557600 * 164.79132) , 2)
