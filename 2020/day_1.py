import random
from copy import deepcopy


def quick_sort(in_list):

    in_list = deepcopy(in_list)

    if len(in_list) <= 1:
        return in_list

    partition_idx = random.randrange(len(in_list))
    partition_elem = in_list.pop(partition_idx)

    left_list = []
    right_list = []

    for elem in in_list:

        if elem <= partition_elem:
            left_list.append(elem)
        else:
            right_list.append(elem)

    return quick_sort(left_list) + [partition_elem] + quick_sort(right_list)


def get_items_from_target_sum(in_list, target_sum):

    in_list = quick_sort(in_list)
    num_items = len(in_list)

    lower_idx = 0
    upper_idx = num_items - 1

    while lower_idx < upper_idx:

        # get elements
        lower = in_list[lower_idx]
        upper = in_list[upper_idx]

        # get target
        upper_target = target_sum - lower

        while upper > upper_target:
            upper_idx -= 1

            if upper_idx <= lower_idx:
                return None

            upper = in_list[upper_idx]

        if upper == upper_target:
            return [lower, upper]
        else:
            lower_idx += 1

    return None


def get_multi_target_sum(in_list, target_sum, num_elems):

    if len(in_list) <= 0:
        return None

    if num_elems == 2:
        return get_items_from_target_sum(in_list, target_sum)

    for idx, elem in enumerate(in_list):

        new_list = in_list[idx+1:]
        new_target = target_sum - elem

        result = get_multi_target_sum(new_list, new_target, num_elems - 1)

        if result:
            result.append(elem)
            return result

    return None


def read_inputs():

    file_path = './inputs/d1_input.txt'

    with open(file_path, 'r') as in_file:
        lines = in_file.readlines()

    in_list = [int(l.strip()) for l in lines]

    return in_list


def get_product(in_list, target, num_elems):

    elements = get_multi_target_sum(in_list, target, num_elems)

    if not elements:
        return None

    product = 1

    for elem in elements:
        product *= elem

    return product


def run():
    test_in_list = [1721, 979, 366, 299, 675, 1456]
    target = 2020
    num_elems = 3

    test_result = get_product(test_in_list, target, num_elems)

    if test_result:
        print("The product is {}".format(test_result))
    else:
        print("No elements summing to {} were found.".format(target))

    actual_in_list = read_inputs()
    #actual_in_list.remove(335)
    actual_result = get_product(actual_in_list, target, num_elems)

    if actual_result:
        print("The product is {}".format(actual_result))
    else:
        print("No elements summing to {} were found.".format(target))

if __name__ == "__main__":
    run()
