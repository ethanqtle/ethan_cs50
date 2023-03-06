import pytest
from twttr import shorten

def test_shorten_lower():
    assert shorten("Twitter") == "Twttr"
    assert shorten("this is a book") == "ths s  bk"

def test_shorten_upper():
    assert shorten("TwIttEr") == "Twttr"
    assert shorten("thIs Is A bOOk") == "ths s  bk"

def test_shorten_num():
    assert shorten("TwiIttEer0124") == "Twttr0124"

def test_shorten_punc():
    assert shorten("thiIs Eis aA ,;()booEEk") == "ths s  ,;()bk"

