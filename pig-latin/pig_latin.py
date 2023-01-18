def translate(text: str):
    """Function for pig latin transformation"""
    new_words = ""
    text = text.split(" ")
    for word in text:
        word_changed = False
        #Rule 1
        if word.startswith("xr") or word.startswith("yt") and not(word_changed):
            new_words += word + "ay" + " "
            word_changed = True
            continue
        if word[0] in ["a","e","i","o","u"] and not(word_changed):
            new_words += word + "ay" + " "
            word_changed = True
            continue
        #Rule 2
        if "qu" not in word and not(word_changed):
            for letter in word:
                if letter in ["a","e","i","o","u"]:
                    vowel_at = word.index(letter)
                    new_words += word[vowel_at:] + word[:vowel_at] + "ay" + " "
                    word_changed = True
                    break
        #Rule 3
        if "qu" in word  and not(word_changed):
            qu_at = word.index("qu")
            new_words += word[qu_at + 2:] + word[:qu_at + 2] + "ay" + " "
            word_changed = True
            continue

        #Rule 4
        if len(word) == 2 and word[1] == "y" and not(word_changed):
            new_words += "y" + word[0] + "ay" + " "
            word_changed = True
            continue
        
        if "y" in word and not(word_changed):
            y_at = word.index("y")
            new_words +=  word[y_at:] + word[:y_at] + "ay" + " "
            word_changed = True

    return new_words.strip()