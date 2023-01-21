"""Implementation of Atbash Cipher"""

LETTERS = "abcdefghijklmnopqrstuvwxyz"

CIPHER_DICT_ENCODE = {num:let for let,num in enumerate(LETTERS)}
CIPHER_DICT_DECODE = dict(zip(range(0,26), LETTERS[::-1]))


def encode(plain_text):
    """Encoding the plain text to cipher"""
    encoded_str_index = []
    for letter in plain_text:
        if letter.lower() in CIPHER_DICT_ENCODE:
            encoded_str_index.append(CIPHER_DICT_ENCODE[letter.lower()])
        else:
            #Replacing original num values as str
            if letter.isnumeric():
                encoded_str_index.append(letter)

    encoded_str = ""
    for index in encoded_str_index:
        if index in CIPHER_DICT_DECODE:
            encoded_str += CIPHER_DICT_DECODE[index]
        else:
            encoded_str += str(index)

    if len(encoded_str) > 5:
        encoded_str_s = [encoded_str[i : i + 5] for i in range(0, len(encoded_str), 5)]
        return " ".join(encoded_str_s)

    return encoded_str


def decode(ciphered_text):
    """Decoding the ciphered text to plain text"""
    decoded_str_index = []
    for letter in ciphered_text:
        if letter in CIPHER_DICT_ENCODE:
            decoded_str_index.append(CIPHER_DICT_ENCODE[letter])
        else:
            #Replacing original num values as str
            if letter.isnumeric():
                decoded_str_index.append(letter)

    decoded_str = ""
    for index in decoded_str_index:
        if index in CIPHER_DICT_DECODE:
            decoded_str += CIPHER_DICT_DECODE[index]
        else:
            decoded_str += str(index)

    return decoded_str
