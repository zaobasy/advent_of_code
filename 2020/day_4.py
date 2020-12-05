
PASSPORT_FIELDS = {
                    'byr' : 'BirthYear',
                    'iyr' : 'IssueYear',
                    'eyr' : 'ExpirationYear',
                    'hgt' : 'Height',
                    'hcl' : 'HairColor',
                    'ecl' : 'EyeColor',
                    'pid' : 'PassportID',
                    'cid' : 'CountryID',
                  }

def check_field(field, value):
    """
    Check that the values matches the fields rules
    """

    if field == 'byr':
        value = int(value)
        return (1920 <= value and value <= 2002)
    elif field == 'iyr':
        value = int(value)
        return (2010 <= value and value <= 2020)
    elif field == 'eyr':
        value = int(value)
        return (2020 <= value and value <= 2030)
    elif field == 'hgt':
        last_two = value[-2:]

        if len(value[:-2]) == 0:
            return False

        value = int(value[:-2])

        if last_two == 'cm':
            return (150 <= value and value <= 193)
        elif last_two == 'in':
            return (59 <= value and value <= 76)
        else:
            return False

    elif field == "hcl":
        if value[0] != '#':
            return False

        if len(value[1:]) != 6:
            return False

        for c in value[1:]:
            if not c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a',
                        'b', 'c', 'd', 'e', 'f']:
                return False

        return True

    elif field in "ecl":
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    elif field in "pid":
        if len(value) != 9:
            return False

        for c in value:
            if not c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return False

        return True

    return

def check_keys(id_dict):
    """
    Check that the appropriate fields exist in the id
    """

    fields_diff = set(PASSPORT_FIELDS.keys()) - set(id_dict.keys())

    if len(fields_diff) == 0:
        return True
    elif len(fields_diff) != 1:
        return False
    else:
        if fields_diff.pop() == 'cid':
            return True

    return False

def check_ids(id_dicts):
    """
    Return the number of valid and invalid ids based on if they have all
    passport fields with the exception of country id (cid)
    """

    valid = 0
    invalid = 0

    for id in id_dicts:

        is_valid = True

        if not check_keys(id):
            invalid += 1
            continue

        for field, value in id.items():

            if field == 'cid':
                continue

            field_check = check_field(field, value)

            if not field_check:
                is_valid = False
                break

        if is_valid:
            valid += 1
        else:
            invalid += 1

    return valid, invalid


def parse_input_to_id_dicts(in_data):
    """
    Takes list of file lines and parses to a list of dictionaries
    one dict per id  field --> value
    """

    id_dicts = []

    num_lines = len(in_data)
    idx = 0

    while idx < num_lines:

        id_dict = dict()
        line = in_data[idx]

        while line != '':
            fields = line.split(' ')

            for field in fields:
                key,value = field.split(":")
                id_dict[key] = value

            idx += 1
            if idx >= num_lines:
                break

            line = in_data[idx]

        id_dicts.append(id_dict)
        idx += 1

    return id_dicts

def read_inputs(path):

    with open(path, 'r') as in_file:
        lines = in_file.readlines()

    return [l.strip() for l in lines]


def run_for_input(path):
    """
    run the calc for id card checking
    print output
    """

    input = read_inputs(path)
    ids = parse_input_to_id_dicts(input)
    valid, invalid = check_ids(ids)

    print("There are {} valid and {} invalid ids".format(valid, invalid))
    return


def run():

    test_path = './inputs/d4_test.txt'
    print("Running on test input")
    run_for_input(test_path)
    print()

    actual_path = './inputs/d4_input.txt'
    print("Running on actual input")
    run_for_input(actual_path)
    print()

if __name__ == "__main__":
    run()
