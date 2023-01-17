"""Honestly no idea how to implement this, was going to use Classes
and linked list to implement the basic structures, apparently just list comprehension. Whoosh ! """


def append(list1, list2):
    """Adds two lists"""
    return list1 + list2


def concat(lists):
    """Combines two lists"""
    concatened_list = []
    for item in lists:
        concatened_list += item
    return concatened_list


def filter(function, lst):
    """Check if func value is true then creates list with True values"""
    mapped_function = []
    for item in lst:
        if function(item):
            mapped_function += [item]
    return mapped_function

def length(lst):
    """Returns length of list provided"""
    number = 0
    for _ in lst:
        number += 1
    return number

def map(function, lst):
    """Returns value of the function applied to each item in list"""
    mapped_function = []
    for item in lst:
        mapped_function.append(function(item))
    return mapped_function


def foldl(function, lst, initial):
    """Left to right operations for functions"""
    res = initial
    for item in lst:
        res = function(res, item)
    return res


def foldr(function, lst, initial):
    """Roght to left operations for functions"""
    res = initial
    for item in reverse(lst):
        res = function(item, res)
    return res


def reverse(lst):
    """Reverse list items"""
    return lst[::-1]
