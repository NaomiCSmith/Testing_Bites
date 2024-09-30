

from lib.report_length import *

def test_report_length_horse():
    result = report_length("horse")
    assert result == (f"This string was 5 characters long.")

def test_report_length_caterpillar():
    result = report_length("caterpillar")
    assert result == (f"This string was 11 characters long.")

def test_report_length_keep_on_going():
    result = report_length("keep-on-going!")
    assert result == (f"This string was 14 characters long.")