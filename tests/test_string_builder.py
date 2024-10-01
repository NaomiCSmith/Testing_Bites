from lib.string_builder import *

def test_string_builder_string():
    string_builder = StringBuilder()
    string_builder.add("Howdy")
    result = string_builder.output()
    assert result == "Howdy"

def test_string_builder_string_and_string():
    string_builder = StringBuilder()
    string_builder.add("Howdy")
    string_builder.add(" cowboy!")
    result = string_builder.output()
    assert result == "Howdy cowboy!"


def test_string_builder_length():
    string_builder = StringBuilder()
    string_builder.add("Howdy cowboy!")
    result = string_builder.size()
    assert result == 13
    


