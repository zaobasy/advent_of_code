

def read_inputs(path):

    with open(path, 'r') as in_file:
        lines = in_file.readlines()

    return [l.strip() for l in lines]


def run_boot_commands(commands):
    """
    Take the input list of commands and run the boot sequence
    """

    boot_done = False
    boot_looped = False

    idx = 0
    total = 0
    done_idx = len(commands)
    visited = set()

    while not (boot_looped or boot_done):

        visited.add(idx)
        cmd, arg = commands[idx]

        if cmd == 'acc':
            total += arg
            idx += 1
        elif cmd == 'jmp':
            idx += arg
        elif cmd == 'nop':
            idx += 1
        else:
            raise ValueError("Unknown command {}".format(cmd))

        if idx in visited:
            boot_looped = True
        elif idx == done_idx:
            boot_done = True

    return total, boot_looped, visited


def parse_to_tuples(command_strs):
    """
    Parse commands into a tuple list
    """
    tuples = []

    for command in command_strs:
        cmd, arg = command.split(" ")
        cmd = cmd.strip()
        arg = int(arg.strip())

        tuples.append((cmd, arg))

    return tuples


def run_for_input(path):
    """
    run calculation
    """

    commands = read_inputs(path)
    commands = parse_to_tuples(commands)

    boot_total, looped, visited = run_boot_commands(commands)

    if looped:
        print("The total was {} when the program looped.".format(boot_total))

    jumps_and_noops = set([i for i in visited
                           if commands[i][0] in ['jmp', 'nop']])

    successful_boot = False

    while jumps_and_noops:

        curr_idx = jumps_and_noops.pop()
        cmd = commands[curr_idx]

        if cmd[0] == 'jmp':
            old = ('jmp', cmd[1])
            commands[curr_idx] = ('nop', cmd[1])
        elif cmd[0] == 'nop':
            old = ('nop', cmd[1])
            commands[curr_idx] = ('jmp', cmd[1])

        boot_total, looped, visited = run_boot_commands(commands)

        if looped:
            commands[curr_idx] = old
        else:
            successful_boot = True
            break

    if successful_boot:
        print("The boot was successful with total {}".format(boot_total))
    else:
        print("No successful boot was found")

    return


def run():

    test_path = './inputs/d8_test.txt'
    print("Running on test input")
    run_for_input(test_path)
    print()

    actual_path = './inputs/d8_input.txt'
    print("Running on actual input")
    run_for_input(actual_path)
    print()


if __name__ == "__main__":
    run()
