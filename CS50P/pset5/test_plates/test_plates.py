import pytest
from plates import is_valid

# Discussion from https://edstem.org/us/courses/176/discussion/2645116

def test_length():
    assert is_valid("") == False
    assert is_valid(" ") == False
    assert is_valid("z") == False
    assert is_valid("abcdefgh") == False
    assert is_valid("ABCDEF") == True

def test_punctuation():
    assert is_valid("AA AA") == False
    assert is_valid("!") == False
    assert is_valid("AX@24") == False

def test_first_letters():
    assert is_valid("01ABCD") == False
    assert is_valid("12ABCD") == False
    assert is_valid("a0abc") == False
    assert is_valid("1ABCD") == False
    assert is_valid("aaa123") == True

def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AA01AA") == False
    assert is_valid("ABCDE0") == False
    assert is_valid("C500") == False