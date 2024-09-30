

from lib.check_codeword import *

def test_check_codeword_returns_correct_if_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_returns_close_for_first_and_last_letters():
    result = check_codeword("hermione")
    assert result == "Close, but nope."

def test_check_codeword_returns_wrong_if_not_horse():
    result = check_codeword("lemons")
    assert result == "WRONG!"