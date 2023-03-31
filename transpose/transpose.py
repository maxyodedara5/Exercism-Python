"""Transposes given lines similar to transpose matrix"""

def transpose(lines):
    """Transposes given lines similar to transpose matrix"""
    lines = lines.split('\n')

    transposed_lines = []
    if len(lines) == 1:
        for item in lines[0]:
            transposed_lines.append(item)
        return "\n".join(transposed_lines)

    no_string = len(lines)
    size_of_lines = {}
    for index,line in enumerate(lines):
        size_of_lines[index] = len(line)

    print(size_of_lines)
    to_make_len = max(size_of_lines.values())
    for index,line in enumerate(lines.copy()):
        if len(line) != to_make_len:
            lines[index] += "*" * (to_make_len - len(line))

    for number in range(to_make_len): #16
        to_add = ""
        for letters in range(no_string): #2
            to_add += lines[letters][number]
        while to_add.endswith("*"):
            to_add = to_add[:-1]
        to_add = to_add.replace("*"," ")

        transposed_lines.append(to_add)

    return "\n".join(transposed_lines)
