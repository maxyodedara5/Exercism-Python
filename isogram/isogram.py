"""Script to check if the string is isogram"""

def is_isogram(string):
    """Check if the string is isogram"""
    string = string.lower()
    if "_" in string or " " in string or "-" in string:
        string = string.replace("_", "")
        string = string.replace(" ", "")
        string = string.replace("-", "")
    original_str_len = len(string)
    reduced_str_len = len(set(string))
    if original_str_len == reduced_str_len:
        return True
    return False
