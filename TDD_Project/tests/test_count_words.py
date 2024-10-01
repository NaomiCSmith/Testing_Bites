from lib.count_words import *

def test_count_words_adam_kay():
    result = count_words("This is going to hurt")
    assert result == 5

def test_count_words_jane_austen():
    result = count_words("Pride and prejudice")
    assert result == 3

def test_count_words_douglas_adams():
    result = count_words("The hitchiker's guide to the galaxy")
    assert result == 6