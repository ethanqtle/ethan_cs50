import pytest
from plates import is_valid

# Discussion from https://edstem.org/us/courses/176/discussion/2645116

def __run_cases(test_cases=[]):
    for plate, expected in test_cases:
        assert is_valid(plate) == expected

def test_length():
    test_cases = [
        ("", False),
        (" ", False),
        ("z", False),
        ("abcdefgh", False),
        ("ABCDEF", True),
    ]
    __run_cases(test_cases)

def test_punctuation():
    test_cases = [
        ("AA AA", False),
        ("!", False),
        ("AX@24", False),
    ]
    __run_cases(test_cases)

def test_first_letters():
    test_cases = [
        ("01ABCD", False),
        ("12ABCD", False),
        ("a0abc", False),
        ("1ABCD", False),
        ("aaa123", True),
    ]
    __run_cases(test_cases)

def test_numbers():
    test_cases = [
        ("AAA222", True),
        ("AAA22A", False),
        ("AA01AA", False),
        ("ABCDE0", False),
        ("C500", False),
    ]
    __run_cases(test_cases)