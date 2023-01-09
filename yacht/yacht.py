"""# score_cal categories."""
# Change the values as you see fit.
YACHT =             "YACHT"
ONES =              "ONES"
TWOS =              "TWOS"
THREES =            "THREES"
FOURS =             "FOURS"
FIVES =             "FIVES"
SIXES =             "SIXES"
FULL_HOUSE =        "FULL_HOUSE"
FOUR_OF_A_KIND =    "FOUR_OF_A_KIND"
LITTLE_STRAIGHT =   "LITTLE_STRAIGHT"
BIG_STRAIGHT =      "BIG_STRAIGHT"
CHOICE =            "CHOICE"


def score(dice, category):
    """Calculates the score of the yatch"""
    dice.sort()
    score_cal = 0
    if category == "YACHT":
        if dice.count(dice[0]) == 5:
            score_cal = 50

    num_of_dies = {
        "ONES" : 1,
        "TWOS" : 2,
        "THREES" : 3,
        "FOURS" : 4,
        "FIVES" : 5,
        "SIXES" : 6
    }
    if category in num_of_dies:
        if dice.count(num_of_dies[category]) != 0 :
            score_cal = num_of_dies[category] * dice.count(num_of_dies[category])


    if category == "FULL_HOUSE":
        first_num = dice.count(dice[0])
        second_num = dice.count(dice[-1])
        if first_num == 3 and second_num == 2:
            score_cal = sum(dice)

        if first_num == 2 and second_num == 3:
            score_cal = sum(dice)

    if category == "FOUR_OF_A_KIND":
        if dice.count(dice[2]) >= 4:
            score_cal = dice[2] * 4

    if category == "BIG_STRAIGHT" and dice == [2,3,4,5,6]:
        score_cal = 30

    if category == "LITTLE_STRAIGHT" and dice == [1,2,3,4,5]:
        score_cal = 30

    if category == "CHOICE":
        score_cal = sum(dice)

    return score_cal
