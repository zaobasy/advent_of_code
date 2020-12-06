import string


def get_group_questions(in_data, check_type):
    """
    Split input into groups and

    check_type = "any" or "all"

    return group selections
    """

    if check_type not in ['any', 'all']:
        raise ValueError('Incorrect Check Type {}'.format(check_type))

    groups = []
    num_lines = len(in_data)
    idx = 0

    while idx < num_lines:

        if check_type == 'any':
            group_qs = set()
        elif check_type == 'all':
            group_qs = set(string.ascii_lowercase)

        line = in_data[idx]

        while line:

            if check_type == 'any':
                group_qs |= set(line)
            if check_type == 'all':
                group_qs &= set(line)

            idx += 1

            if idx == num_lines:
                break

            line = in_data[idx]

        groups.append(group_qs)

        idx += 1

    return groups


def read_inputs(path):

    with open(path, 'r') as in_file:
        lines = in_file.readlines()

    return [l.strip() for l in lines]


def run_for_input(path):
    """
    run calculation
    """

    in_data = read_inputs(path)

    any_groups = get_group_questions(in_data, 'any')
    num_qs = sum([len(g) for g in any_groups])
    print('Total number of yesses that anyone in group answered {}'.format(
        num_qs))

    all_groups = get_group_questions(in_data, 'all')
    num_qs = sum([len(g) for g in all_groups])
    print('Total number of yesses that all in group answered {}'.format(num_qs))

    return


def run():

    test_path = './inputs/d6_test.txt'
    print("Running on test input")
    run_for_input(test_path)
    print()

    actual_path = './inputs/d6_input.txt'
    print("Running on actual input")
    run_for_input(actual_path)
    print()


if __name__ == "__main__":
    run()
