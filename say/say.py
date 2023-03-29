"""Says number to words"""

number_dict = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
}

three_zeroes_behind = {
    0 : "",
    1 : " thousand",
    2 : " million",
    3 : " billion",
    4 : " trillion"
}


def double_digits(double_str):
    """Returns string of passed number """

    number = int(double_str)

    if 0 <= number <= 20:
        return number_dict[number]

    if number % 10 == 0:
        return number_dict[number]

    first_digit = int(double_str[0]) * 10
    second_digit = int(double_str[1])
    number_str = number_dict[first_digit] + "-" + number_dict[second_digit]
    return number_str


def split_large_num(number):
    """Returns list of split numbers, splits numbers in digits of 3"""
    str_number = str(number)

    # 3 is splitting in digits of 3 if another number change 3
    missing_zeros = len(str_number) % 3
    if missing_zeros != 0:
        str_number = (3 - missing_zeros) * '0' + str_number

    nums = []
    for i in range(len(str_number)//3):
        nums.append(str_number[i*3: i*3 + 3])

    return nums

def convert_3_digits_to_words(three_dig_num, zereos):
    """convert_3_digits_to_words"""

    first_digit = three_dig_num[0]
    num_string_first_part = number_dict[int(first_digit)] + " hundred "
    if "zero" in num_string_first_part:
        num_string_first_part = ""

    num_string_sec_part = double_digits(three_dig_num[1:]) + three_zeroes_behind[zereos]
    if "zero" in num_string_sec_part:
        num_string_sec_part = ""

    return num_string_first_part + num_string_sec_part


def say(number):
    """Says number to words"""

    if number < 0:
        raise ValueError("input out of range")

    if number > 999999999999:
        raise ValueError("input out of range")

    if 0 <= number <= 20:
        return number_dict[number]

    if 20 < number < 100:
        number = str(number)
        return double_digits(number)

    # Large nums
    nums = split_large_num(number)
    words = ""
    for zereos, num in enumerate(nums):
        zereos = len(nums) - zereos - 1
        words += convert_3_digits_to_words(num, zereos) + " "

    return words.strip()
