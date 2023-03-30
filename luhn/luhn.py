"""Creates Luhn class"""

class Luhn:
    """Creates Luhn class"""
    def __init__(self, card_num):
        self.card_num = card_num
        self.valid_flag = None
        self.num_ints = []
        self.invalid_chars = ""
        for digit in self.card_num:
            if digit.isdigit() or digit.isspace():
                if digit.isdigit():
                    self.num_ints.append(int(digit))
            else:
                self.invalid_chars += digit

    def valid(self):
        """Checks if number is valid"""
        if self.valid_flag is True:
            return True

        if len(self.invalid_chars) > 0:
            return False

        if len(self.num_ints) < 2:
            return False

        self.num_ints.reverse()
        for index,_ in enumerate(self.num_ints):
            if index % 2 != 0:
                self.num_ints[index] = self.num_ints[index] * 2

        for index,_ in enumerate(self.num_ints):
            if self.num_ints[index] > 9:
                self.num_ints[index] = self.num_ints[index] - 9

        if sum(self.num_ints) % 10 == 0:
            self.valid_flag = True
            return True

        return False
