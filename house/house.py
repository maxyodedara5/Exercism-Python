"""A bad exercise to explain recursion where it is not needed"""

INPUT_POEM_PHRASES = [
"the horse and the hound and the horn that belonged to ",
"the farmer sowing his corn that kept ",
"the rooster that crowed in the morn that woke ",
"the priest all shaven and shorn that married ",
"the man all tattered and torn that kissed ",
"the maiden all forlorn that milked ",
"the cow with the crumpled horn that tossed ",
"the dog that worried ",
"the cat that killed ",
"the rat that ate ",
"the malt that lay in ",
"the house that Jack built."
]


def recite(start_verse, end_verse):
    """Some poem implementation that is supposed to show how recursion works"""
    # Not sure of the correct implementation insufficient documentation
    if start_verse == end_verse:
        answer_string = "This is "
        answer_verses = INPUT_POEM_PHRASES[-(start_verse):]
        answer_string += "".join(answer_verses)
        return [answer_string]

    #  We assume that this means lines from start to end verse
    ans_verses = []
    if start_verse != end_verse:
        for i in range(start_verse, end_verse + 1):
            answer_string = "This is "
            answer_verses = INPUT_POEM_PHRASES[-(i):]
            answer_string += "".join(answer_verses)
            ans_verses.append(answer_string)
    return ans_verses
