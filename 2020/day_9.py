from day_1 import get_multi_target_sum


def read_inputs(path):

    with open(path, 'r') as in_file:
        lines = in_file.readlines()

    return [int(l.strip()) for l in lines]


def XMAS_error_finder(in_list, xmas_size):
    """
    Find the first number not following the xmas scheme
    """

    list_len = len(in_list)

    for idx in range(list_len-xmas_size):

        current_list = in_list[idx:idx+xmas_size]
        current_target = in_list[idx+xmas_size]

        found_sum = get_multi_target_sum(current_list, current_target, 2)

        if not found_sum:
            break

    return current_target


def find_rolling_sum(in_list, target):
    """
    Find the set of contiguous numbers summing to target
    """

    size = 2
    list_len = len(in_list)

    while size < list_len:

        for idx in range(list_len-size):
            test_list = in_list[idx:idx+size]

            if sum(test_list) == target:
                return test_list

        size += 1

    return None


def run_for_input(path, xmas_size):
    """
    run calculation
    """

    in_list = read_inputs(path)
    error_value = XMAS_error_finder(in_list, xmas_size)

    print("The first xmas error was found: {}".format(error_value))

    # divide list into two parts partitioned by error
    idx = in_list.index(error_value)
    list1 = in_list[:idx]
    list2 = in_list[idx+1:]

    # check list1 first (likely result is here since numbers are smaller)
    summed_values = find_rolling_sum(list1, error_value)

    if not summed_values:
        summed_values = find_rolling_sum(list2, error_value)

    print("Found contiguous elements that sum to error: {}".format(
        summed_values))

    print("The extrema values sum to {}".format(min(summed_values) +
                                                max(summed_values)))

    return


def run():

    xmas_size = 5
    test_path = './inputs/d9_test.txt'
    print("Running on test input")
    run_for_input(test_path, xmas_size)
    print()

    xmas_size = 25
    actual_path = './inputs/d9_input.txt'
    print("Running on actual input")
    run_for_input(actual_path, xmas_size)
    print()


if __name__ == "__main__":
    run()
