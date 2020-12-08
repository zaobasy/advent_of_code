import re


def parse_to_dictionary(in_data):
    """
    Take input text and parse it to a dictionary
    of bags
    """

    out_dict = dict()
    digit_regex = re.compile('^\d+')

    for line in in_data:

        main_bag, contains = line.split("contain")
        main_bag = main_bag.strip()

        cont_split = contains.split(",")
        cont_split = [b.strip('.').strip() for b in cont_split]

        cont_bags = []

        for bag in cont_split:

            digit_match = digit_regex.match(bag)

            if digit_match:
                digit = int(digit_match.group())
                span = digit_match.span()
                bag_name = bag[span[1]:].strip()

                if bag_name[-1] != 's':
                    bag_name = '{}s'.format(bag_name)

                cont_bags.append((digit, bag_name))


        out_dict[main_bag] = cont_bags

    return out_dict


def invert_dictionary(in_dict):
    """
    For main_bag -> bags inside, invert to
    bag_name -> contained by bags
    """

    inverted_dict = dict()

    for main_bag, contains_bags in in_dict.items():

        if main_bag not in inverted_dict:
            inverted_dict[main_bag] = set()

        for _num, bag in contains_bags:

            if bag not in inverted_dict:
                inverted_dict[bag] = set([main_bag])
            else:
                inverted_dict[bag].add(main_bag)

    return inverted_dict


def find_all_that_contain_bag(bag_name, bag_dict):
    """
    Find all larger bags that can contain 'bag_name' where bag_dict
    maps bags -> all bags that can contain it
    """

    # basically breadth first search
    to_process = bag_dict.get(bag_name)
    found_bags = set()

    while len(to_process) > 0:

        curr_bag = to_process.pop()

        if curr_bag not in found_bags:
            found_bags.add(curr_bag)
            to_process |= set(bag_dict.get(curr_bag))

    return found_bags


def num_bags_inside(bag_name, in_dict):
    """
    Determine how many bags are contained inside your bag
    """

    contained_bags = in_dict.get(bag_name)

    if not contained_bags:
        return 0

    total_bags = 0

    for num, bag in contained_bags:
        total_bags += num*(1 + num_bags_inside(bag, in_dict))

    return total_bags

def read_inputs(path):

    with open(path, 'r') as in_file:
        lines = in_file.readlines()

    return [l.strip() for l in lines]


def run_for_input(path, bag_name):
    """
    run calculation
    """

    in_data = read_inputs(path)

    bag_dict = parse_to_dictionary(in_data)
    inverted_dict = invert_dictionary(bag_dict)

    all_contains = find_all_that_contain_bag(bag_name, inverted_dict)

    print("There are {} bags that can hold {}".format(len(all_contains),
                                                     bag_name))

    total_bags = num_bags_inside(bag_name, bag_dict)
    print("Your {} will hold {} total bags".format(bag_name, total_bags))

    return


def run():

    bag_name = 'shiny gold bags'

    test_path = './inputs/d7_test.txt'
    print("Running on test input")
    run_for_input(test_path, bag_name)
    print()

    actual_path = './inputs/d7_input.txt'
    print("Running on actual input")
    run_for_input(actual_path, bag_name)
    print()


if __name__ == "__main__":
    run()
