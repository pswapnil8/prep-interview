import pytest
from coding_interview_snippets import (
    reverse_string,
    reverse_number,
    is_palindrome,
    flatten_list,
    get_longest_even,
    length_of_longest_substring,
    two_sum,
    move_zeros_to_end,
    max_difference,
)


def test_reverse_string():
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("abc") == "cba"


def test_reverse_number():
    assert reverse_number(123) == 321
    assert reverse_number(-45) == -54


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal, Panama")
    assert is_palindrome("racecar")
    assert not is_palindrome("hello")


def test_flatten_list():
    assert flatten_list([[1, 2], [3, [4, 5]]]) == [1, 2, 3, 4, 5]
    assert flatten_list([]) == []


def test_get_longest_even():
    s = "This test has four even word abcd efgh!"
    result = get_longest_even(s)
    # Result should be alphabetic and have even length
    assert result.isalpha()
    assert len(result) % 2 == 0


def test_length_of_longest_substring():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("") == 0


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_move_zeros_to_end():
    assert move_zeros_to_end([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_max_difference():
    assert max_difference([7, 1, 5, 3, 6, 4]) == 5
    assert max_difference([5]) is None
