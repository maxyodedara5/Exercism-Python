from datetime import timedelta

def add(moment):
    "Adds 10 ^ 9 seconds to the time given"
    return moment + timedelta(seconds=10E8)
