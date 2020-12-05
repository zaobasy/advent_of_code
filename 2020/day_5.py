


def parse_seat_to_binary(seat):
    """
    Take a seat identifier BFFFBBFRRR and determine it's binary
    number
    """

    replaces = {
                'B' : '1',
                'F' : '0',
                'R' : '1',
                'L' : '0',
                }

    out_str = seat

    for old, new in replaces.items():
        out_str = out_str.replace(old, new)

    return out_str

def read_inputs(path):

    with open(path, 'r') as in_file:
        lines = in_file.readlines()

    return [l.strip() for l in lines]


def print_debug_for_input(path):
    """
    print input, binary number, and decimal
    print output
    """

    input = read_inputs(path)

    for line in input:
        binary = parse_seat_to_binary(line)
        decimal = int(binary, 2)

        print("Input {} : binary {}  : decimal {}".format(line, binary,
                                                          decimal))
    return

def run_for_input(path):
    """
    run calculation
    """

    input = read_inputs(path)

    all_possible_seats = range(2**len(input[0]))
    seat_nos = set([int(parse_seat_to_binary(seat), 2)
                    for seat in input])

    print("The max seat is {}".format(max(seat_nos)))

    missing_seats = set(all_possible_seats) - seat_nos

    extra_seats = []

    for seat in missing_seats:

        if (seat - 1 in seat_nos) and (seat + 1 in seat_nos):
            extra_seats.append(seat)

    print("Here are empty seats {}".format(extra_seats))


def run():

    test_path = './inputs/d5_test.txt'
    print("Running on test input")
    print_debug_for_input(test_path)
    run_for_input(test_path)
    print()

    actual_path = './inputs/d5_input.txt'
    print("Running on actual input")
    run_for_input(actual_path)
    print()


if __name__ == "__main__":
    run()
