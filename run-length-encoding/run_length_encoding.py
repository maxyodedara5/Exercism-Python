"""Encode Decode functions for Run-Length Encoding"""

def decode(to_decode):
    """Decodes to RLE"""
    if len(to_decode) <= 1:
        return to_decode

    new_string = ""
    for index, letter in enumerate(to_decode[:-1]):
        new_string += letter
        if letter.isalpha() and to_decode[index+1].isdigit():
            new_string += ":"
        elif letter.isspace() and (to_decode[index+1].isdigit() or to_decode[index+1].isalpha()):
            new_string += ":"
        elif letter.isalpha() and (to_decode[index+1].isalpha() or to_decode[index+1].isspace()):
            if letter != to_decode[index+1]:
                new_string += ":"
    new_string += to_decode[-1]

    decods = new_string.split(":")
    decoded_str = ""
    for word in decods:
        if len(word) != 1:
            decoded_str += int(word[:-1]) * word[-1]
        else:
            decoded_str += word[0]
    return decoded_str

def encode(to_encode):
    """Encodes to RLE """
    if len(to_encode) <= 1:
        return to_encode

    new_string = ""
    for index, letter in enumerate(to_encode[:-1]):
        new_string += letter
        if letter != to_encode[index+1]:
            new_string += ":"
    new_string += to_encode[-1]

    encods = new_string.split(":")
    encoded_str = ""
    for word in encods:
        if word.count(word[0]) != 1:
            encoded_str += str(word.count(word[0])) + word[0]
        else:
            encoded_str += word[0]
    return encoded_str
