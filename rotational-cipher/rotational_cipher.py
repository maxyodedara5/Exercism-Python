"""Ceaser Cipher Implementation"""

def rotate(text, key):
    """Ceaser Cipher Implementation"""
    let_num = {num:let for num,let in enumerate("abcdefghijklmnopqrstuvwxyz")}
    text_dict = {let:num + key for num,let in enumerate(text)}
    text_dict = {}
    for let in text:
        if let.lower() not in let_num.values():
            continue
        text_dict[let.lower()] = list(let_num.keys())[list(let_num.values()).index(let.lower())]
        text_dict[let.lower()] += key

    for i in text_dict:
        if text_dict[i] >= 26:
            text_dict[i] = text_dict[i] % 26
        text_dict[i] = let_num.get(text_dict[i])
        if text_dict[i] is None:
            text_dict[i] = i

    ans = ""
    for letter in text:
        if letter.lower() in let_num.values():
            if letter.isupper():
                ans += text_dict[letter.lower()].upper()
            else:
                ans += text_dict[letter.lower()]
        else:
            ans += letter

    return ans
