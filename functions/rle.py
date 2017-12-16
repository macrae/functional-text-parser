import numpy as np
from functools import reduce


def listify_string(string):
    """
    Put each character in a string into a list.

    Args:
        string (Str):          string to listify

    Returns:
        list (Str):            list of characters in string
    """
    return list(map(lambda x: x, string))


def get_pairs(l):
    """
    Group consecutive elements of a list, into a list of 2-tuples.

    Args:
        list (Str):             list of elements

    Returns:
        list (Tuple):           list of 2-tuples
    """
    return list(zip(l, l[1:]))


def compare_pairs(pairs):
    """
    Compare each 2-tuple in a list (x, y) for equality (x == y).

    Args:
        list (Tuples):          list of 2-tuples

    Returns:
        list (Booleans):        list of booleans
    """
    return [x == 0 for x in list(
        map(lambda x: hash(x[0]) - hash(x[1]), pairs))]


def get_break_points(pair_comparison):
    """
    Get index of 2-tuple inequality (x != y) as indicator of character change.

    Args:
        list (Booleans):          list of booleans

    Returns:
        list (Int):               list of indices for character changes
    """
    index_equal_pairs = list(
        zip(np.arange(0, len(pair_comparison)), pair_comparison))

    breaks = list(filter(lambda x: x[1] == False, index_equal_pairs))

    break_points = list(map(lambda x: x[0] + 1, breaks))

    break_points = [0] + break_points + [len(pair_comparison) + 1]

    return break_points


def break_list(list, break_points):
    """
    Given a list and indices of consecutive character breaks for that list,
    generate a list of lists containing the consecutive characters.

    Args:
        list (String):                 list of characters in a string
        break_points (List[Int])

    Returns:
        list (Tuples):            list of 2-tuples
    """
    new_list = []

    for item in get_pairs(break_points):
        new_list.append(list[item[0]:item[1]])

    return new_list


def aggregate_broken_list(broken_list):

    list_of_counts = list(map(lambda x: str(len(x)) + str(x[0]), broken_list))

    string_of_counts = reduce(lambda accum, elem: accum + elem, list_of_counts)

    return string_of_counts


def rle(string):

    l = listify_string(string)

    break_points = get_break_points(compare_pairs(get_pairs(l)))

    return aggregate_broken_list(break_list(l, break_points))
