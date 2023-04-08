from um import count


def test_count_word():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Hello, um, world") == 1


def test_count_sentence():
    assert count("This is, um... CS50.") == 1
    assert count("Um... what are regular expressions?") == 1
    assert count("Um, thanks, um, regular expressions make sense now.") == 2


def test_count_um_in_word():
    assert count("Um, thanks for the album.") == 1
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2