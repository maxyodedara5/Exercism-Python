"""Square cipher implementation"""

def cipher_text(plain_text):
    """Square cipher implementation"""
    # Cleaning the string
    final_string = ""
    for letter in plain_text:
        if letter.isalpha() or letter.isnumeric():
            final_string += letter.lower()

    # Find rectange co ordinates
    grid_found = True
    col = 0
    row = 0
    row_add = False
    while grid_found:
        if col * row >= len(final_string):
            grid_found = False
            break
        if row_add:
            row_add = False
            row += 1
        else:
            row_add = True
            col += 1
    #print(col, row)

    # Pad parent string with spaces
    if len(final_string) != col * row:
        final_string = final_string + " " * ((col * row) - len(final_string))

    rows = []
    for i in range(row):
        rows.append(final_string[i * col : (i * col) + 8])

    ciphered_text = []
    for i in range(col):
        cipher_col = ""
        for j in range(row):
            #print(rows[j][i],end="")
            cipher_col += rows[j][i]
        ciphered_text.append(cipher_col)

    # print(" ".join(ciphered_text))
    # for i in range(row):
    #     for j in range(col):
    #         print(i,j,end="\t")
    #     print()
    print(len(" ".join(ciphered_text)))
    return " ".join(ciphered_text)
