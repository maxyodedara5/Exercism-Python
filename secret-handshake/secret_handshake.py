"""Script for conversion"""

def commands(binary_str):
    """Binary for conversion"""

    hand_shake = []
    if binary_str[-1] == "1":
        hand_shake.append("wink")
    if binary_str[-2] == "1":
        hand_shake.append("double blink")
    if binary_str[-3] == "1":
        hand_shake.append("close your eyes")
    if binary_str[-4] == "1":
        hand_shake.append("jump")
    if binary_str[-5] == "1":
        hand_shake.reverse()

    return hand_shake
