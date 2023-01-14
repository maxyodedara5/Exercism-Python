"""Script for flatting a list"""

def flatten(iterable):
    """Flattens a list"""
    elements = []
    for ele in iterable:
        if isinstance(ele,list):
            inside_elements = flatten(ele)
            elements.extend(inside_elements)
        else:
            if ele is not None:
                elements.append(ele)
    return elements
