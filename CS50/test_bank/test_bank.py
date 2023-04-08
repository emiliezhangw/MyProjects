from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("How you doing?") == 20
    assert value("What's up") == 100


def test_caseinsensitivity():
    assert value("hello") == 0
    assert value("How you doing?") == 20
    assert value("What's up") == 100


def test_entirephrase():
    assert value("Hello, what can I help you?") == 0
    assert value("How you doing?") == 20
    assert value("What's up") == 100
