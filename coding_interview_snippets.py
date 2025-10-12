def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_number(n):
    reverse = 0
    num = n
    while num > 0:
        remainder = num % 10
        reverse = (reverse * 10) + remainder
        num = num // 10
    return reverse

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def is_digit_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def find_max_element(lst):
    if not lst:
        return None
    max_element = lst[0]
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element

def find_min_element(lst):
    if not lst:
        return None
    min_element = lst[0]
    for num in lst:
        if num < min_element:
            min_element = num
    return min_element

def remove_duplicates(input_string):
    unique_chars = set()
    result = ""
    for char in input_string:
        if char not in unique_chars:
            result += char
            unique_chars.add(char)
    return result