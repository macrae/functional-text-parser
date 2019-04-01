from functools import reduce
from typing import List

import numpy as np


def listify_string(s: str) -> List[str]:
    """Create a list of characters from a string
    """
    return list(map(lambda x: x, s))


def group_consecutive_elements(l: list) -> List[tuple]:
    """Group consecutive elements of a list into a list of tuples
    """
    return list(zip(l, l[1:]))


def compare_tuples(t: List[tuple]):
    """Compare each tuple in a list (x, y) for equality (x == y).
    """
    return [x == 0 for x in list(map(lambda x: hash(x[0]) - hash(x[1]), t))]


def get_break_points(pair_comparison: List[tuple]):
    """Get index of tuple inequality (x != y) as indicator of character change.
    """
    index_equal_pairs = list(zip(np.arange(0, len(pair_comparison)), pair_comparison))
    breaks = list(filter(lambda x: x[1] == False, index_equal_pairs))
    break_points = list(map(lambda x: x[0] + 1, breaks))
    break_points = [0] + break_points + [len(pair_comparison) + 1]
    return break_points


def break_list(list: List, break_points):
    """Given a list and indices of consecutive character breaks for that list,
    generate a list of lists containing the consecutive characters.
    """
    new_list = []
    for item in group_consecutive_elements(break_points):
        new_list.append(list[item[0] : item[1]])
    return new_list


def aggregate_broken_list(broken_list):
    list_of_counts = list(map(lambda x: str(len(x)) + str(x[0]), broken_list))
    string_of_counts = reduce(lambda accum, elem: accum + elem, list_of_counts)
    return string_of_counts


def rle(string):
    l = listify_string(string)
    break_points = get_break_points(compare_tuples(group_consecutive_elements(l)))
    return aggregate_broken_list(break_list(l, break_points))
