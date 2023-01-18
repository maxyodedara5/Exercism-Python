"""Long division method, my proudest code for Exercism so far. Good exercise"""

def square_root(number):
    """Finds the square root of number using long division method"""

    # Creating pairs
    digits = len(str(number))
    number = str(number)
    num_pairs = []
    pairs = digits // 2

    if digits % 2 == 0:
        for i in range(pairs):
            num_pairs.append(number[i * 2: i * 2 + 2])
    else:
        to_add_later = number[0]
        number = number[1:]
        num_pairs.append("0" + to_add_later)
        for i in range(pairs):
            num_pairs.append(number[i * 2: i * 2 + 2])

    num_on_left = ""
    current_num = int(num_pairs[0])
    first_time = True
    sq_root = []

    while len(num_pairs) != 0:
        find_closest_mul = 0
        closest_mul = 0
        if first_time:
            while closest_mul <= current_num:
                find_closest_mul += 1
                if find_closest_mul * find_closest_mul > current_num:
                    find_closest_mul -= 1
                    sq_root.append(str(find_closest_mul))
                    break
                closest_mul = find_closest_mul * find_closest_mul
                first_time = False

            #First time operation skip
            pending_number = current_num - closest_mul
            num_pairs.pop(0)
            if len(num_pairs) == 0:
                break
            current_num = int(str(pending_number) + num_pairs[0])
            num_on_left = find_closest_mul + find_closest_mul

        else:
            while closest_mul <= current_num:
                find_closest_mul += 1
                mul = find_closest_mul * int(str(num_on_left) + str(find_closest_mul))
                if mul > current_num:
                    find_closest_mul -= 1
                    sq_root.append(str(find_closest_mul))
                    break
                closest_mul = find_closest_mul * int(str(num_on_left) + str(find_closest_mul))

            pending_number = current_num - closest_mul
            num_pairs.pop(0)
            if len(num_pairs) == 0:
                break
            current_num = int(str(pending_number) + num_pairs[0])

            # Sideoperations
            num_on_left = int(str(num_on_left) + str(find_closest_mul))


    return int("".join(sq_root))
