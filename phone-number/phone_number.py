"""Class for Phone number generation accroding to North American Numbering Plan (NANP)"""

class PhoneNumber:
    """Phone number generation accroding to North American Numbering Plan (NANP)"""
    number = ""
    incorrect_str = ""
    area_code = ""


    def __init__(self, number):
        for c_h in number:
            if c_h.isdecimal():
                self.number += c_h
            else:
                if c_h in "abcdefghijklmnopqrstuvwxyz":
                    raise ValueError("letters not permitted")

                if c_h in "!@#$%^&*_=~:;',/?><":
                    raise ValueError("punctuations not permitted")

        # if a phone number has less than 10 digits.
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        # if a phone number has more than 11 digits.
        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")

        # if a phone number has 11 digits, but starts with a number other than 1.
        if len(self.number) == 11 and self.number[0] != "1":
            raise ValueError("11 digits must start with 1")

        if len(self.number) == 11:
            # 1 - 123 - 1234567
            # 0 - 123 - 45678910
            # if a phone number has an exchange code that starts with 0.
            if self.number[4] == "0":
                raise ValueError("exchange code cannot start with zero")

        # if a phone number has an exchange code that starts with 1.
            if self.number[4] == "1":
                raise ValueError("exchange code cannot start with one")

        # if a phone number has an area code that starts with 0.
            if self.number[1] == "0":
                raise ValueError("area code cannot start with zero")

        # if a phone number has an area code that starts with 1.
            if self.number[1] == "1":
                raise ValueError("area code cannot start with one")


        if len(self.number) == 10:
            # 1 - 123 - 1234567
            # 0 - 123 - 45678910
            # if a phone number has an exchange code that starts with 0.
            if self.number[3] == "0":
                raise ValueError("exchange code cannot start with zero")

        # if a phone number has an exchange code that starts with 1.
            if self.number[3] == "1":
                raise ValueError("exchange code cannot start with one")

        # if a phone number has an area code that starts with 0.
            if self.number[0] == "0":
                raise ValueError("area code cannot start with zero")

        # if a phone number has an area code that starts with 1.
            if self.number[0] == "1":
                raise ValueError("area code cannot start with one")

        if len(self.number) == 11:
            self.number = self.number[1:]
            self.area_code = self.number[1:4]
        else:
            self.area_code = self.number[0:3]

    def pretty(self):
        """Preties your number"""
        if len(self.number) == 11:
            return f"({self.number[1:4]})-{self.number[4:7]}-{self.number[7:]}"
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"
