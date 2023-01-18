def abbreviate(words):
    itr = 0
    acronym = ""
    sepfound = True
    while(itr < len(words)):
        if words[itr].isalpha():
            acronym += words[itr].upper()
            sepfound = False
        else:
            itr += 1
            sepfound = True 
        while not sepfound and itr < len(words):
            if words[itr] == " " or words[itr] == "-":
                sepfound = True
            itr += 1

    return acronym