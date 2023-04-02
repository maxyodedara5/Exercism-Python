"""Converts string of nums to rows and columns in matrix"""

class Matrix:
    """Converts string of nums to rows and columns in matrix"""
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = []
        self.columns = []

        # Create rows first, column depends on this block
        rows_string = self.matrix_string.split("\n")
        for num, row in enumerate(rows_string):
            rows_string[num] = row.split(" ")
            rows_string[num] = [int(x) for x in rows_string[num]]

        self.rows = rows_string

    def row(self, index):
        """Gets needed row from matrix"""
        return self.rows[index - 1]

    def column(self, index):
        """Gets needed column from matrix"""
        for row_num, _ in enumerate(self.rows[0]):
            current_cols = []
            for col, _ in enumerate((self.rows)):
                current_cols.append(self.rows[col][row_num])
            self.columns.append(current_cols)

        return self.columns[index-1]
