from lib.make_snippet import *

def test_make_snippet_frog():
    result = make_snippet("Today I ate a frog from the garden pond.")
    assert result == "Today I ate a frog..."

def test_make_snippet_fly():
    result = make_snippet("I wish I could fly like a pigeon or a mosquito.")
    assert result == "I wish I could fly..."

def test_make_snippet_jumped():
    result = make_snippet("The quick brown fox jumped over the lazy dog.")
    assert result == "The quick brown fox jumped..."