import pytest
from lib.present import *

def test_present_contents_have_been_wrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap()
        error_message = str(e.value)
        assert error_message == (f"A contents has already been wrapped.")

def test_no_present_contents_is_wrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
        error_message = str(e.value)
        assert error_message == (f"No contents have been wrapped.")