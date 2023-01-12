"""# How default args work"""

def two_fer(name = "you"):
    """Uses default when name not provided"""
    return f"One for {name}, one for me."
