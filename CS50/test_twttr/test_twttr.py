from twttr import shorten

# Test capitalized vowel replacement
def test_capitalize():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("WHAT'S YOUR NAME?") == "WHT'S YR NM?"


# Test lowercase vowel replacement
def test_lowerecase():
    assert shorten("twitter") == "twttr"
    assert shorten("what's your name?") == "wht's yr nm?"


# Test omitting numbers
def test_numbers():
    assert shorten("CS50") == "CS50"


# Test omitting punctuation
def test_punctuation():
    assert shorten("Hello, world") == "Hll, wrld"
    assert shorten("What's your name?") == "Wht's yr nm?"
