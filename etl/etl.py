"""Script for transforming data from legacy to new data form"""

def transform(legacy_data):
    """Transform data from legacy to new data form"""
    # {1: ['A']}
    # {'a': 1}
    new_data = {}
    for item in legacy_data:
        for value_in_item in legacy_data[item]:
            new_data[value_in_item.lower()] = item

    return new_data
