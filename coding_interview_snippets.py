"""Collection of small interview-prep functions exported from the
Practice.ipynb notebook.

Each function is small and pure-Python so it can be unit-tested.
"""

from typing import List, Optional, Sequence, Tuple


def reverse_string(s: str) -> str:
    """Return the reverse of the given string.

    Args:
        s: Input string.
    Returns:
        Reversed string.
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


def reverse_number(num: int) -> int:
    """Reverse the digits of an integer preserving sign.

    Examples:
        reverse_number(123) -> 321
        reverse_number(-45) -> -54
    """
    result = 0
    n = abs(num)
    while n > 0:
        result = result * 10 + (n % 10)
        n //= 10
    return result if num >= 0 else -result


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (ignore non-alphanumerics and case)."""
    filtered = ''.join(filter(str.isalnum, s)).lower()
    return filtered == filtered[::-1]


def flatten_list(nested_list: Sequence) -> List:
    """Recursively flatten a nested list/sequence into a flat list."""
    flat: List = []
    for item in nested_list:
        if isinstance(item, list) or isinstance(item, tuple):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


def get_longest_even(sentence: str) -> str:
    """Return the longest even-length word from sentence (ignore punctuation).

    If multiple words tie, the first encountered is returned. Returns empty string
    when none found.
    """
    longest = ""
    for word in sentence.split():
        clean = ''.join(ch for ch in word if ch.isalpha())
        if len(clean) % 2 == 0 and len(clean) > len(longest):
            longest = clean
    return longest


def length_of_longest_substring(s: str) -> int:
    """Return the length of the longest substring without repeating characters."""
    window = []
    max_len = 0
    for ch in s:
        if ch in window:
            window = window[window.index(ch) + 1 :]
        window.append(ch)
        if len(window) > max_len:
            max_len = len(window)
    return max_len


def two_sum(nums: Sequence[int], target: int) -> Optional[List[int]]:
    """Return indices of two numbers that add up to target (first match).

    Returns None if no pair found.
    """
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            return [seen[comp], i]
        seen[n] = i
    return None


def move_zeros_to_end(lst: Sequence[int]) -> List[int]:
    """Return a new list with zeros moved to the end, preserving order."""
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros


def max_difference(nums: Sequence[int]) -> Optional[int]:
    """Return the maximum (nums[j] - nums[i]) where j>i. None if not applicable."""
    if len(nums) < 2:
        return None
    min_val = float('inf')
    max_diff = float('-inf')
    for n in nums:
        min_val = min(min_val, n)
        max_diff = max(max_diff, n - min_val)
    return max_diff


__all__ = [
    "reverse_string",
    "reverse_number",
    "is_palindrome",
    "flatten_list",
    "get_longest_even",
    "length_of_longest_substring",
    "two_sum",
    "move_zeros_to_end",
    "max_difference",
]
