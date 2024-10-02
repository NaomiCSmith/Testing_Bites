from lib.grammar_checker import *

def test_grammar_checker_capital_no_punct():
    result = grammar_checker("Hello world")
    assert result == "Not quite! This text starts with a capital letter but is missing suitable ending punctuation."

def test_grammar_checker_puntuation_no_capital():
    result = grammar_checker("not the polar bears!")
    assert result == "Not quite! This text does not start with a capital letter but does end with suitable punctuation."


def test_grammar_checker_capital_and_punct():
    result = grammar_checker("Watch out for the bees?")
    assert result == "Good job! This text starts with a capital letter and ends with suitable punctuation."

def test_grammar_checker_neither():
    result = grammar_checker("even the snakes think so")
    assert result == "Oh no! This sentence needs a capital letter to start and suitable ending punctuation."