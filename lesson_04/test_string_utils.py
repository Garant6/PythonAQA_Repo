import pytest
from string_utils import StringUtils


@pytest.mark.parametrize( "in_text, result", [ ("hello", "Hello"), ("What", "What"), ("my book", "My book")])
def test_positive_capitalize(in_text, result):
    capitalize = StringUtils()
    assert capitalize.capitalize(in_text) == result

@pytest.mark.xfail
@pytest.mark.parametrize("in_text, result", [ ("", ""), (".", "."), ("   ff", "   Ff"), ("123", "123"), ([], "")])
def test_negative_capitalize(in_text, result):
    capitalize = StringUtils()
    assert capitalize.capitalize(in_text) == result
""" Заглавной делает не первую букву, а первый символ. Видно по негативным тестам(последний).
Первый символ пробел его и делает заглавным. А первую букву F не делает. """

@pytest.mark.parametrize("in_text, result", [ ("   Hello", "Hello"), ("  space", "space"), ("   Go home", "Go home"),
("  123245", "123245")])
def test_trim(in_text, result):
    trim = StringUtils()
    assert trim.trim(in_text) == result

@pytest.mark.xfail
@pytest.mark.parametrize("in_text, result", [ ([], ""), ("", ""), ("   ", "")])
def test_negative_trim(in_text, result):
    trim = StringUtils()
    assert trim.trim(in_text) == result

@pytest.mark.parametrize("in_text, symbol, result", [ ("Hello!", "H", True), ("Bottle", "P", False), ("   ", " ", True),
("Pumpkin!!!", "!", True), ("From China", "i", True)])
def test_positive_contains(in_text, symbol, result):
    contain = StringUtils()
    assert contain.contains(in_text, symbol) == result

@pytest.mark.xfail
@pytest.mark.parametrize("in_text, symbol, result", [ ("One", "", False), ("", "A", False), ([], "", False)])
def test_negative_contains(in_text, symbol, result):
    contain = StringUtils()
    assert contain.contains(in_text, symbol) == result

@pytest.mark.parametrize("in_text, symbol, result", [ ("Hello", "l", "Heo"), ("First!!!!", "!", "First"), 
("AAA", "A", ""), ("AoAAooaO", "AA", "AoooaO"), ("In Brazil", "l", "In Brazi")])
def test_positive_delete_symbol(in_text, symbol, result):
    del_sym = StringUtils()
    assert del_sym.delete_symbol(in_text, symbol) == result

@pytest.mark.xfail
@pytest.mark.parametrize("in_text, symbol, result", [ (" ", " ", ""), ([], "", ""), ("", "", "")])
def test_negative_delete_symbol(in_text, symbol, result):
    del_sym = StringUtils()
    assert del_sym.delete_symbol(in_text, symbol) == result
