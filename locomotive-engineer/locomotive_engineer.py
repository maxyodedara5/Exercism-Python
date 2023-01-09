"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first_id , second_id, *rest = each_wagons_id
    first_item_from_rest , *rest = rest
    new_list = [first_item_from_rest, *missing_wagons, *rest, first_id, second_id]
    return new_list


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops = []
    for value in kwargs.values():
        stops.append(value)

    route["stops"] = stops
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    combined_route_info = {**route, **more_route_information}
    return combined_route_info


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [[term_0, term_1, term_2], [term_3, term_4, term_5], [term_6, term_7 ,term_8]] = wagons_rows
    # a term_1 term_2
    # term_3 e term_5
    # g term_7 term_8
    term_1, term_3 = term_3, term_1
    term_2, term_6 = term_6, term_2
    term_5, term_7 = term_7, term_5
    wagons_rows = [[term_0, term_1, term_2], [term_3, term_4, term_5], [term_6, term_7 ,term_8]]
    return wagons_rows
