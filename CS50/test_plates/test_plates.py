from plates import is_valid

def test_beginning_alphabetical():
    assert is_valid("CS50") == True
    assert is_valid("C5012") == False


def test_lenth():
    assert is_valid("CS50P") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False


def test_periods_spaces_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("H,") == False
    assert is_valid("OUT ATIME") == False
