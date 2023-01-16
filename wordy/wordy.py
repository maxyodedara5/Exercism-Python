"""Script for evaluation of sentence math left to right regardless of logic"""

def answer(question: str):
    """Function for evaluation of sentence math left to right regardless of logic"""

    question = question.replace("?","")
    question = question.replace("What is ","")
    question = question.replace("What is","")
    question = question.replace("multiplied by","multipliedby")
    question = question.replace("divided by","dividedby")


    args = question.split(" ")
    if len(args) == 1:
        if not args[0].isnumeric():
            raise ValueError("syntax error")
        return int(args[0])


    for i,_ in enumerate(args):
        if args[i].startswith("-") or args[i].isnumeric():
            if i % 2 != 0:
                raise ValueError("syntax error")
            args[i] = int(args[i])
            continue
        if args[i] not in ["plus","minus","multipliedby", "dividedby"]:
            raise ValueError("unknown operation")

    if len(args) % 2 == 0:
        raise ValueError("syntax error")

    result = args[0]
    while len(args) != 1:
        if args[1] == "multipliedby":
            mul_at = 1
            result = args[mul_at - 1] * args[mul_at + 1]
            del args[mul_at - 1: mul_at + 2]
            args.insert(mul_at -1 ,result)
            continue

            # or "dividedby" in args:
        if args[1] == "dividedby":
            mul_at = 1
            result = args[mul_at - 1] / args[mul_at + 1]
            del args[mul_at - 1: mul_at + 2]
            args.insert(mul_at -1 ,result)
            continue

        if args[1] == "plus":
            mul_at = 1
            result = args[mul_at - 1] + args[mul_at + 1]
            del args[mul_at - 1: mul_at + 2]
            args.insert(mul_at -1 ,result)
            continue

        if args[1] == "minus":
            mul_at = 1
            result = args[mul_at - 1] - args[mul_at + 1]
            del args[mul_at - 1: mul_at + 2]
            args.insert(mul_at -1 ,result)

    return args[0]
