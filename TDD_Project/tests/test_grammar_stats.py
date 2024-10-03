from lib.grammar_stats import *

def test_class_initiates():
    pass

def test_check_capital_and_punct_true():
    grammar = GrammarStats()
    assert grammar.check("Can you please pick me up some self-esteem from the shops?") == True

def test_check_capital_and_punct_false_both():
    grammar = GrammarStats()
    assert grammar.check("noooooooo thank youuuuuuu") == False

def test_check_capital_and_punct_false_no_punct():
    grammar = GrammarStats()
    assert grammar.check("There's a cat over there&") == False

def test_check_capital_and_punct_false_no_cap():
    grammar = GrammarStats()
    assert grammar.check("perhaps we should reconsider hot air balloons for our commute!") == False

def test_percentage_good_50():
    grammar = GrammarStats()
    grammar.check("there's aliens on jupiter?")
    grammar.check("people need to chill out")
    grammar.check("Give me the passports, I don't trust you.")
    grammar.check("Just because you have a pet snail, it doesn't mean you can communicate with them!")
    assert grammar.percentage_good() == 50

def test_percentage_good_75():
    grammar = GrammarStats()
    grammar.check("there's aliens on jupiter?")
    grammar.check("People need to chill out!")
    grammar.check("Give me the passports, I don't trust you.")
    grammar.check("Just because you have a pet snail, it doesn't mean you can communicate with them!")
    assert grammar.percentage_good() == 75

def test_percentage_good_0():
    grammar = GrammarStats()
    grammar.check("there's aliens on jupiter?")
    grammar.check("people need to chill out!")
    grammar.check("Give me the passports, I don't trust you")
    grammar.check("just because you have a pet snail, it doesn't mean you can communicate with them!")
    assert grammar.percentage_good() == 0

def test_percentage_good_100():
    grammar = GrammarStats()
    grammar.check("There's aliens on jupiter?")
    grammar.check("People need to chill out!")
    grammar.check("Give me the passports, I don't trust you.")
    grammar.check("Just because you have a pet snail, it doesn't mean you can communicate with them!")
    assert grammar.percentage_good() == 100