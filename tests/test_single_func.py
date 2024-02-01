from lib.single_func import *

def test_make_snippet_returns_string():
    actual = make_snippet('Hello, this is your friend Ray!')
    expected = 'Hello, this is your friend ...'
    assert actual == expected

def test_make_snippet_argument_less_than_5_words():
    actual = make_snippet('Hello there')
    expected = 'Sentence too short'
    assert actual == expected

def test_count_words():
    actual = count_words('Hello there')
    expected = 2
    assert actual == expected