"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return (coordinate[0], coordinate[1])



def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    a_co_ordinate = azara_record[1]
    a_co_ordinate = (a_co_ordinate[0], a_co_ordinate[1])

    if a_co_ordinate == rui_record[1]:
        return True
    return False


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible),
    or the string "not a match" (if incompatible).
    """
    combined_record = "not a match"
    if azara_record[1] == "".join(rui_record[1]):
        combined_record = azara_record + rui_record

    return combined_record


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    ans_tuples = []
    for record in combined_record_group:
        ans_tuple_str = (record[0], record[2], record[3], record[4])
        ans_tuples.append(ans_tuple_str)

    ans_string = "\n".join(str(rec) for rec in ans_tuples)
    ans_string += "\n"
    return ans_string
