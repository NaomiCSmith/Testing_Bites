

from lib.greet import *

def test_greet_returns_hello_with_name():
    result = greet("Naomi")
    assert result == (f"Hello, Naomi!")