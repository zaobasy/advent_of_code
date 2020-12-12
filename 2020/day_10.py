from day_1 import quick_sort


def read_inputs(path):

    with open(path, 'r') as in_file:
        lines = in_file.readlines()

    return [int(l.strip()) for l in lines]


def find_jolts_between_all(in_list):
    """
    Do a dumb thing and just assume to use all adapters we just loop in
    sorted order.
    """
    possible_diffs = [1,2,3]

    distribution = {d:0 for d in possible_diffs}
    sorted_list = quick_sort(in_list)

    # add in your adaptor
    sorted_list.append(sorted_list[-1] + 3)

    prev_jolts = 0

    for jolts in sorted_list:

        diff = jolts - prev_jolts
        prev_jolts = jolts

        if diff in possible_diffs:
            distribution[diff] += 1
        else:
            raise ValueError("You made a dumb assumption that didn't work")

    return distribution


def count_number_of_arrangements(in_list):
    """
    Calculate how many ways to connect between the wall and your phone
    """

    possible_diffs = [1,2,3]

    # get sorted list with your phone too
    sorted_list = quick_sort(in_list)
    sorted_list.append(sorted_list[-1] + 3)

    # There is a clear recursion. let:
    #
    # f(N) = number of arrangements connecting the wall (0) to N
    # adapt(N) = is there an adaptor for joltage N (0 = no, 1 = yes)
    #
    # f(N) = adapt(N-1)*f(N-1) + adapt(N-2)*f(N-2) + adapt(N-3)*f(N-3)
    #
    # This will be super slow because you might recalculate f(small Ns)
    # many times. So instead let's use dynamic programming and cache results
    # starting at low N

    arrange_dict = dict()

    for adaptor in sorted_list:

        arrangements = 0

        for diff in possible_diffs:

            old_jolts = adaptor - diff

            if old_jolts < 0:
                arrangements += 0
            elif old_jolts == 0:
                arrangements += 1
            else:
                arrangements += arrange_dict.get(old_jolts, 0)

        arrange_dict[adaptor] = arrangements

    return arrange_dict


def run_for_input(path):
    """
    run calculation
    """

    in_list = read_inputs(path)
    dist = find_jolts_between_all(in_list)

    print("The distribution is {}".format(dist))
    print("The product of 1 and 3 is {}".format(dist[1]*dist[3]))

    arrange_dict = count_number_of_arrangements(in_list)
    #print(arrange_dict)
    print("The number of ways to connect is {}".format(arrange_dict[max(
                                                       arrange_dict.keys())]))

    return


def run():

    test_path = './inputs/d10_test.txt'
    print("Running on test input")
    run_for_input(test_path)
    print()

    actual_path = './inputs/d10_input.txt'
    print("Running on actual input")
    run_for_input(actual_path)
    print()


if __name__ == "__main__":
    run()
