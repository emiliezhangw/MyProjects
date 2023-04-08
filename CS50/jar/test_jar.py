from jar import Jar
from pytest import raises

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(6)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    with raises(ValueError):
        jar.deposit(17)

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    with raises(ValueError):
        jar.withdraw(8)
