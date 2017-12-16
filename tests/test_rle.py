import os
import sys

sys.path.insert(0, os.path.abspath('./functions'))

from rle import *

string = 'AABBCDDDE'


def test_listify_string():
    l = listify_string(string)

    assert l == ['A', 'A', 'B', 'B', 'C', 'D', 'D', 'D', 'E']


def test_get_pairs():
    pairs = get_pairs(listify_string(string))

    assert pairs == [('A', 'A'), ('A', 'B'), ('B', 'B'), ('B', 'C'),
                     ('C', 'D'), ('D', 'D'), ('D', 'D'), ('D', 'E')]


def test_compare_pairs():
    comparisons = compare_pairs(get_pairs(listify_string(string)))

    assert comparisons == [True, False, True, False, False, True, True, False]


def test_get_break_points():
    break_points = get_break_points(
        compare_pairs(get_pairs(listify_string(string))))

    assert break_points == [0, 2, 4, 5, 8, 9]


def test_break_list():
    break_points = get_break_points(
        compare_pairs(get_pairs(listify_string(string))))

    broken_list = break_list(listify_string(string), break_points)

    assert broken_list == [['A', 'A'], [
        'B', 'B'], ['C'], ['D', 'D', 'D'], ['E']]


def test_aggregate_broken_list():
    break_points = get_break_points(
        compare_pairs(get_pairs(listify_string(string))))

    broken_list = break_list(listify_string(string), break_points)

    aggregate = aggregate_broken_list(broken_list)

    assert aggregate == '2A2B1C3D1E'


def test_rle():
    assert rle('A') == '1A'
    assert rle('AA') == '2A'
    assert rle('AAAB') == '3A1B'
    assert rle('AAABB55') == '3A2B25'
