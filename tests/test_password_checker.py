import pytest
from lib.password_checker import *

def test_password_checker_invalid_length():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordchecker.check()
        error_message = str(e.value)
        assert error_message == "Invalid password, must be 8+ characters."