"""Decimal to Roman conversion"""

UNITS = {
    0 : "",
    1 : "I",
    2 : "II",
    3 : "III",
    4 : "IV",
    5 : "V",
    6 : "VI",
    7 : "VII",
    8 : "VIII",
    9 : "IX"
}

def roman(number):
    """Decimal to Roman conversion"""
    thousands = number % 10000 // 1000
    hundreds = number % 1000 // 100
    tens = number % 100 // 10
    digits = number % 10

    roman_hundreds = UNITS[hundreds]
    roman_hundreds = roman_hundreds.replace("X","M")
    roman_hundreds = roman_hundreds.replace("I","C")
    roman_hundreds = roman_hundreds.replace("V","D")

    roman_tens = UNITS[tens]
    roman_tens = roman_tens.replace("X","C")
    roman_tens = roman_tens.replace("I","X")
    roman_tens = roman_tens.replace("V","L")

    roman_num = thousands * "M" + roman_hundreds + roman_tens +  UNITS[digits]
    return roman_num
