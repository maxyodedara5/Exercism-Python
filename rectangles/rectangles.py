"""Gives number of rectangles in a grid of + | - """

def check_diagonal(fix_point, diagonal_points, all_points, grid_string):
    """Checks whether the points are of square"""
    f_x, f_y = fix_point
    rects = 0
    for d_x, d_y in diagonal_points:
        if not (((f_x, d_y) in all_points) and ((d_x, f_y) in all_points)):
            continue

        # Check grid
        # Top line and Bottom line
        x_fail = False
        for x_check in range(f_x, d_x + 1):
            if (grid_string[x_check][f_y] not in ['+','|']) or \
            (grid_string[x_check][d_y] not in ['+','|']):
                x_fail = True
                break

        # Left and Right line
        y_fail = False
        for y_check in range(f_y, d_y + 1):
            if (grid_string[f_x][y_check] not in ['+','-']) or \
            (grid_string[d_x][y_check] not in ['+','-']):
                y_fail = True
                break

        if not x_fail and not y_fail:
            rects += 1

    return rects

def rectangles(strings):
    """Gives number of rectangles in a grid of + | - """
    row_len = len(strings)
    if row_len == 0:
        return 0
    col_len = len(strings[0])

    co_ords = []
    for row in range(row_len):
        for col in range(col_len):
            if strings[row][col] == "+":
                co_ords.append((row, col))

    current_index = 0
    total_rectangles = 0
    for cur_x, cur_y in co_ords:
        diagonal_list = []
        for i_x, i_y in co_ords:
            if i_x > cur_x and i_y > cur_y:
                current_index += 1
                diagonal_list.append((i_x, i_y))
        total_rectangles += check_diagonal((cur_x, cur_y), diagonal_list, co_ords, strings)

    return total_rectangles
