"""Clock class implementation"""

class Clock:
    """Clock class implementation"""
    def __init__(self, hour, minute):
        self.hour = hour % 24
        self.minute = minute % (24 * 60)
        hour_add = 0
        if self.minute > 59:
            hour_add = self.minute // 60
            self.minute %= 60

        self.hour += hour_add
        self.hour = self.hour % 24

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        str_hour = str(self.hour)
        str_minute = str(self.minute)
        if len(str_hour) < 2:
            if self.hour == '0':
                str_hour = '00'
            else:
                str_hour = '0' + str_hour

        if len(str_minute) < 2:
            if self.minute == '0':
                str_minute = '00'
            else:
                str_minute = '0' + str_minute

        return f"{str_hour}:{str_minute}"

    def __eq__(self, other):
        if other.hour == self.hour and other.minute == self.minute:
            return True
        return False

    def __add__(self, minutes):
        total_minutes = self.minute + minutes
        hour_rollover = total_minutes // 60
        self.hour += hour_rollover
        self.hour = self.hour % 24
        self.minute = total_minutes % 60

        return self.__str__()

    def __sub__(self, minutes):
        total_time = self.hour * 60 + self.minute
        minutes = minutes % (24 * 60)
        total_time =  total_time - minutes
        if total_time - minutes < 0:
            total_time += 1440

        self.hour = total_time // 60
        self.hour = self.hour % 24
        self.minute = total_time % 60
        return self.__str__()
