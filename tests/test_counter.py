from lib.counter import *

def test_counter_starts_zero():
    counter = Counter()
    counter.add(4)
    result = counter.report()
    assert result == f"Counted to 4 so far."

def test_counter_adds_five():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_counter_adds_eleven():
    counter = Counter()
    counter.add(11)
    result = counter.report()
    assert result == "Counted to 11 so far."