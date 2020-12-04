import numpy as np


EMPTY = "."
TREE = "#"

def parse_input_to_array(input):
    """
    Take a list of strings and parse to a tree array
    0 == empty spot
    1 == tree
    """

    # Probably could leave as bools but visualization for debugging is
    # easier with ints
    map_list = [[(c == TREE) for c in line] for line in input]
    map_array = np.array(map_list, dtype=int)

    return map_array


def read_inputs(path):

    with open(path, 'r') as in_file:
        lines = in_file.readlines()

    return [l.strip() for l in lines]


def get_visited_spots(map_array, num_right, num_down):
    """
    Given map and the number of spaces to the right and down each step takes
    return a list of squares you visit before reaching the bottom

    Start is top left and map repeats to right.

    returns visites_coords, visited_squares
    ex [(0,0), (1,5) ,...], [0,0,0,1,0,1,0]
    Note first square is start
    """

    rows, cols = np.shape(map_array)
    slope = np.array([num_down, num_right])

    visited_coords = []
    visited_squares = []
    current = np.array([0,0])


    while current[0] < rows:
        visited_coords.append(tuple(current))
        visited_squares.append(map_array[tuple(current)])
        current += slope

        # loop map around
        current[1] = current[1] % cols

    return visited_coords, visited_squares


def run_for_input(path, slopes_list):
    """
    run the calc for map in path and listed slopes
    print output
    """

    input = read_inputs(path)
    map_array = parse_input_to_array(input)
    out_trees = []

    for slope in slopes_list:
        coords, squares = get_visited_spots(map_array, slope[1], slope[0])

        num_trees = sum(squares)
        num_empty = len(squares) - num_trees
        print("Slope {}: There are {} trees and {} empty spots".format(slope,
                                                                       num_trees,
                                                                       num_empty))

        out_trees.append(num_trees)

    return out_trees


def run():

    # (down, left)
    slopes = [(1,1), (1, 3), (1,5), (1,7), (2,1)]

    test_path = './inputs/d3_test.txt'
    print("Running on test input")
    trees = run_for_input(test_path, slopes)
    print("Product of trees = {}".format(np.prod(trees)))
    print()

    actual_path = './inputs/d3_input.txt'
    print("Running on actual input")
    trees = run_for_input(actual_path, slopes)
    print("Product of trees = {}".format(np.prod(trees)))
    print()



if __name__ == "__main__":
    run()
