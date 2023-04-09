"""Gives which hand won at poker"""

RANKINGS = ["ROYALFLUSH", "STRAIGHTFLUSH", "FOUROFAKIND", "FULLHOUSE", "FLUSH",
            "STRAIGHT", "THREEOFAKIND", "TWOPAIR", "PAIR", "HIGHCARD"]

ORDERED_CARDS = "A,2,3,4,5,6,7,8,9,10,J,Q,K,A"
CARDS = ORDERED_CARDS.split(',')
HIGH_CARDS = sorted(['10', 'J', 'Q', 'K', 'A'])

CARDS_DICT = {card:rank for rank,card in enumerate(CARDS, 1)}


# Logic for checking if the card is of specific type

def card_info(hand):
    """Gives card types and cards"""
    card_types = []
    cards = []
    for card in hand.split(" "):
        card_types.append(card[-1])
        cards.append(card[:-1])
    return card_types, cards


def check_royalflush(hand):
    """Check Royalflush"""
    card_types, cards = card_info(hand)
    all_same_suit = False
    if card_types.count(card_types[0]) == 5:
        all_same_suit = True

    high_cards = False
    if HIGH_CARDS == sorted(cards):
        high_cards = True

    return all_same_suit and high_cards

def check_flush(hand):
    """Check flush"""
    card_types, _ = card_info(hand)
    all_same_suit = False
    if card_types.count(card_types[0]) == 5:
        all_same_suit = True
    return all_same_suit


def check_straight(hand):
    """Check straight"""
    _, cards = card_info(hand)
    # Order of cards
    ordered_cards = []
    for card in CARDS:
        if card in cards:
            ordered_cards.append(card)

    in_sequence = False
    possible_seq = ",".join(ordered_cards)
    if possible_seq.endswith('A') and possible_seq[-3:] != 'K,A':
        possible_seq = possible_seq[:-2]

    if possible_seq.startswith('A') and possible_seq[-3:] == 'K,A':
        possible_seq = possible_seq[2:]

    if possible_seq in ORDERED_CARDS:
        in_sequence = True
    return in_sequence


def check_straightflush(hand):
    """Check straight flush"""
    all_same_suit = check_flush(hand)
    in_sequence = check_straight(hand)
    return all_same_suit and in_sequence


def check_four_of_kind(hand):
    """Checks four of kind"""
    _, cards = card_info(hand)
    cards.sort()
    if cards.count(cards[2]) == 4:
        return True
    return False


def check_full_house(hand):
    """Check full house"""
    full_house_flag = False
    _, cards = card_info(hand)
    cards_count_dict = {}
    for card in cards:
        if card in cards_count_dict:
            cards_count_dict[card] += 1
        else:
            cards_count_dict[card] = 1

    # Check if only 2 types of cards
    num_of_cards = []
    if len(cards_count_dict) == 2:
        num_of_cards = list(cards_count_dict.values())
        num_of_cards.sort()
        if num_of_cards[0] == 2 and num_of_cards[1] == 3:
            full_house_flag = True

    return full_house_flag


def check_only_flush(hand):
    """Check only flush"""
    if check_flush(hand) and not check_straight(hand):
        return True
    return False


def check_only_straight(hand):
    """Check only straight"""
    if check_straight(hand) and not check_flush(hand):
        return True
    return False


def check_three_kind(hand):
    """Check three of a kind"""
    three_kind_flag = False
    _, cards = card_info(hand)
    card_type_dict = {}
    for card_type in cards:
        if card_type in card_type_dict:
            card_type_dict[card_type] += 1
        else:
            card_type_dict[card_type] = 1

    num_types = list(card_type_dict.values())
    num_types.sort()
    if num_types[-1] == 3:
        three_kind_flag = True

    return three_kind_flag


def check_two_pair(hand):
    """Check two pair"""
    two_pair_flag = False
    _, cards = card_info(hand)
    cards_dict = {}
    for card in cards:
        if card in cards_dict:
            cards_dict[card] += 1
        else:
            cards_dict[card] = 1

    nums = list(cards_dict.values())
    nums.sort()
    if len(nums) == 3:
        if nums[-2] == nums[-1] == 2:
            two_pair_flag = True

    return two_pair_flag


def check_pair(hand):
    """Check pair"""
    single_pair_flag = False
    _, cards = card_info(hand)
    cards_dict = {}
    for card in cards:
        if card in cards_dict:
            cards_dict[card] += 1
        else:
            cards_dict[card] = 1

    nums = list(cards_dict.values())
    nums.sort()
    if len(nums) == 4:
        if nums[-1] == 2:
            single_pair_flag = True

    return single_pair_flag


RANKINGS_DICT = {
    "ROYALFLUSH" : check_royalflush, 
    "STRAIGHTFLUSH" : check_straightflush, 
    "FOUROFAKIND" : check_four_of_kind, 
    "FULLHOUSE" : check_full_house, 
    "FLUSH" : check_flush,
    "STRAIGHT" : check_straight, 
    "THREEOFAKIND" : check_three_kind, 
    "TWOPAIR" : check_two_pair, 
    "PAIR" : check_pair,
    }


def check_highcard(hand):
    """Check high card"""
    high_card_flag = True
    for func in RANKINGS_DICT.values():
        if func(hand):
            high_card_flag = False

    return high_card_flag

# Comparing different types of same rank hands
# e.g. Comparing  2 Highcards, 2 pair hands etc


# High Card score logic
def give_highcard_score(hand):
    """Check highcard"""
    _, cards = card_info(hand)
    highest_card = 0
    for card in cards:
        if CARDS_DICT[card] > highest_card:
            highest_card = CARDS_DICT[card]
    return highest_card

#TODO Check if can merge with pair_comparison func
def highcards_comparison(hands):
    """Compares multiple high cards"""
    score_dict = {}

    for hand in hands:
        if give_highcard_score(hand) in score_dict:
            score_dict[give_highcard_score(hand)].append(hand)
        else:
            score_dict[give_highcard_score(hand)] = [hand]

    return score_dict[max(list(score_dict.keys()))]


# pair_comparison works for single pair, 2 pair and 3 pair scores
def pair_score(hand):
    """Pair score"""
    _, cards = card_info(hand)
    cards_dict = {}
    for card in cards:
        if card in cards_dict:
            cards_dict[card] += 1
        else:
            cards_dict[card] = 1

    other_cards = ""
    pair_value = ""
    for card in cards_dict: # pylint: disable=C0206
        if cards_dict[card] in [2,3]:
            pair_value += card
        else:
            other_cards += card

    # Converting other cards to the scored numbered version
    ordered_other_cards = ""
    for card in CARDS[:-1][::-1]:
        if card in other_cards:
            if CARDS_DICT[card] < 10:
                ordered_other_cards += "0" + str(CARDS_DICT[card])
            else:
                ordered_other_cards += str(CARDS_DICT[card])

    # Adding pair score to score string
    ordered_pair = ""
    for card in CARDS[:-1][::-1]:
        if card in pair_value:
            if CARDS_DICT[card] < 10:
                ordered_pair += "0" + str(CARDS_DICT[card])
            else:
                ordered_pair += str(CARDS_DICT[card])

    other_cards = ordered_pair + ordered_other_cards
    return other_cards


def pair_comparison(hands):
    """Pair compairson works for multiple comparison functions"""
    hand_dict = {}
    for hand in hands:
        hand_score = pair_score(hand)
        if hand_score not in hand_dict:
            hand_dict[hand_score] = [hand]
        else:
            hand_dict[hand_score].append(hand)

    return hand_dict[max(list(hand_dict.keys()))]


# Straight comparison
def straight_score(hand):
    """Straight hand score"""
    ordered_hand = ""
    _, cards = card_info(hand)
    for card in CARDS:
        if card in cards:
            ordered_hand += card

    return str(CARDS_DICT[ordered_hand[2]])

#TODO CAn be merged with pair comparison
def straight_comparison(hands):
    """Straight comparison"""
    hand_dict = {}
    for hand in hands:
        hand_score = straight_score(hand)
        if hand_score not in hand_dict:
            hand_dict[hand_score] = [hand]
        else:
            hand_dict[hand_score].append(hand)

    return hand_dict[max(list(hand_dict.keys()))]


# Full house score
def full_house_score(hand):
    """Full house score"""
    _, cards = card_info(hand)
    cards.sort()

    score_cards = ""
    if cards.count(cards[0]) in [3,4] :
        score_cards = cards[0] + " " + cards[-1]
    else:
        score_cards = cards[-1] + " " + cards[0]

    score_string = ""
    for card in score_cards.split():
        if CARDS_DICT[card] < 10:
            score_string += "0" + str(CARDS_DICT[card])
        else:
            score_string += str(CARDS_DICT[card])

    return score_string

def full_house_comparison(hands):
    """Full_house_comparison"""
    hand_dict = {}
    for hand in hands:
        hand_score = full_house_score(hand)
        if hand_score not in hand_dict:
            hand_dict[hand_score] = [hand]
        else:
            hand_dict[hand_score].append(hand)

    return hand_dict[max(list(hand_dict.keys()))]


def straightflush_score(hand):
    """Gives score for straight flush"""
    _, cards = card_info(hand)
    ordered_cards = []
    for card in CARDS:
        if card in cards:
            ordered_cards.append(card)

    score_string = ""
    if CARDS_DICT[ordered_cards[2]] < 10:
        score_string += "0" + str(CARDS_DICT[ordered_cards[2]])
    else:
        score_string += str(CARDS_DICT[ordered_cards[2]])

    return score_string

def straightflush_comparison(hands):
    """Straightflush_comparison"""
    hand_dict = {}
    for hand in hands:
        hand_score = straightflush_score(hand)
        if hand_score not in hand_dict:
            hand_dict[hand_score] = [hand]
        else:
            hand_dict[hand_score].append(hand)

    return hand_dict[max(list(hand_dict.keys()))]

def royalflush_comparison(hands):
    """Royalflush comparison"""
    return hands

COMPARISON_RANKINGS_DICT = {
    "1000000000" : royalflush_comparison,
    "0100000000" : straightflush_comparison,
    "0010000000" : full_house_comparison,
    "0001000000" : full_house_comparison,
    "0000100000" : pair_comparison,
    "0000010000" : straight_comparison,
    "0000001000" : pair_comparison,
    "0000000100" : pair_comparison,
    "0000000010" : pair_comparison,
    "0000000001" : pair_comparison
    }


def give_score_hand(hand):
    """Gives a 10 digit string in order as per RANKINGS"""
    score_string = ""
    for func in RANKINGS_DICT.values():
        if func(hand):
            score_string += "1"
            break
        else:
            score_string += "0"

    score_string = score_string + "0" * (len(RANKINGS_DICT) - len(score_string))

    if check_highcard(hand):
        score_string += "1"
    else:
        score_string += "0"

    return score_string


def best_hands(hands):
    """Gives the hands which are highest ranked"""
    no_of_hands = len(hands)

    if no_of_hands == 1:
        return hands

    score_dict = {}
    for hand in hands:
        score_hand = give_score_hand(hand)
        if score_hand in score_dict:
            score_dict[score_hand].append(hand)
        else:
            score_dict[score_hand] = [hand]


    highest_ranking_hands = score_dict[max(list(score_dict.keys()))]
    highest_rank_key = max(list(score_dict.keys()))
    if len(highest_ranking_hands) > 1:
        #Logic if multiple hands of same score
        highest_ranking_hands = COMPARISON_RANKINGS_DICT[highest_rank_key](highest_ranking_hands)
    return highest_ranking_hands
