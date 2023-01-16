def steps(number):

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    collatz = number
    steps_to_come_here = 0
    while(collatz != 1):
        if collatz % 2 == 0:
            collatz = collatz // 2 
        else:
            collatz = collatz * 3 + 1
        steps_to_come_here += 1
    return steps_to_come_here

