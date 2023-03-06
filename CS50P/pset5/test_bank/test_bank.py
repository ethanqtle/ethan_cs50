import pytest

from bank import value

def test_bank_hello():
    assert(value("hello world")) == 0
    assert(value("HellO world")) == 0

def test_bank_just_partial():
    assert(value("Hey")) == 20
    assert(value("Halleluya")) == 20

def test_bank_missed():
    assert(value("THis is funny")) == 100
    assert(value("no problem")) == 100
