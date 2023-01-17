"""Binary Search implementation"""

def find(search_list, value):
    """Binary Search implementation"""
    if value not in search_list:
        raise ValueError("value not in array")

    found = False
    mid = len(search_list) // 2
    start = 0
    end = len(search_list) - 1
    while not found:
        if search_list[mid] == value:
            found = True
            return mid
        if value > search_list[mid]:
            start = mid + 1
            mid = abs((start - end ) // 2) + start
            continue
        if value < search_list[mid]:
            end = mid - 1
            mid = end // 2
            continue
