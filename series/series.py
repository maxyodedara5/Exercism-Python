"""Slicing practice"""



def slices(series, length):
    """Slicing practice"""
    # if the slice length is zero.
    if length == 0:
        raise ValueError("slice length cannot be zero")

    # if the slice length is negative.
    if length < 0:
        raise ValueError("slice length cannot be negative")

    # if the series provided is empty.
    if series == "":
        raise ValueError("series cannot be empty")

    # if the slice length is longer than the series.
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    number_in_series = len(series)
    out_nums = number_in_series - length + 1

    output = []
    for i in range(0, out_nums):
        output.append(series[i: i + length])
    
    return output