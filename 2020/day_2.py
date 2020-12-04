
def get_counts(password):
    """
    Take a password string and return a counts dictionary
    """

    count_dict = dict()

    for character in password:

        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1

    return count_dict

def check_char_counts(password, left, right, in_char):
    """
    Check if password is valid based on if char count falls in range [left,
    right] (inclusive)

    returns bool (True = valid password)
    """

    pwd_counts = get_counts(password)

    target_count = pwd_counts.get(in_char, 0)

    if left <= target_count and target_count <= right:
        return True

    return False


def check_chars_in_positions(password, left, right, in_char):
    """
    Check if password is valid based on if char count is in exactly one of
    position left or position right

    returns bool (True = valid password)
    """

    is_in_left = password[left-1] == in_char
    is_in_right = password[right-1] == in_char

    # need to xor the two
    return is_in_left != is_in_right

def get_valid_and_invalid_lists(in_list, checker):
    """
    Take a list of strings and return two lists valid_pwds, invalid_pwds
    based on checker.

    signature of checker(password, left, right, in_char)
    """

    valid_pwds = []
    invalid_pwds = []

    for line in in_list:

        rule, password = line.split(":")
        config, in_char = rule.split(" ")
        left, right = config.split("-")

        left = int(left)
        right = int(right)
        password = password.strip()
        in_char = in_char.strip()

        is_valid = checker(password, left, right, in_char)

        if is_valid:
            valid_pwds.append(password)
        else:
            invalid_pwds.append(password)

    return valid_pwds, invalid_pwds


def read_inputs():

    file_path = './inputs/d2_input.txt'

    with open(file_path, 'r') as in_file:
        lines = in_file.readlines()

    return [l.strip() for l in lines]

def run():

    #checker_function = check_char_counts
    checker_function = check_chars_in_positions

    test_input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    valid, invalid = get_valid_and_invalid_lists(test_input, checker_function)

    print("There are {} valid and {} invalid passwords".format(len(valid),
                                                               len(invalid)))

    actual_input = read_inputs()
    valid, invalid = get_valid_and_invalid_lists(actual_input,
                                                  checker_function)

    print("There are {} valid and {} invalid passwords".format(len(valid),
                                                               len(invalid)))


if __name__ == "__main__":
    run()
