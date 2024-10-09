from lib.tdd_is_todo import *

#3 Create examples as tests

# If given two strings in list, and one features #TODO:
# # returns one string with #TODO
# notes : ["#TODO", "todo"]
# def if_todo(notes) == ['#TODO']

def test_returns_only_string_with_TODO():
    notes = ["#TODO", "a string"]
    assert if_todo(notes) == ["#TODO"]


# if given two strings in a list and none contain #TODO:
# returns empty list
## notes : ["TODO", "todo"]
# def if_todo(notes) == []

def test_returns_empty_list_if_no_TODO():
    notes = ["todo", "not todo"]
    assert if_todo(notes) == []

#if given two strings adn both contain #TODO:
# return both strings
# notes : ["TODO", "#TODO"]
# def if_todo(notes) == ["#TODO", "#TODO"]

def test_returns_both_strings_with_TODO():
    notes = ["#TODO feed the cat", "Don't forget #TODO homework"]
    assert if_todo(notes) == ["#TODO feed the cat", "Don't forget #TODO homework"]