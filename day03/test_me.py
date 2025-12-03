'''
Unit tests
'''

import pytest

from . import *

from . import __main__ as tmain


@pytest.fixture
def sample():
    '''Sample data, one list item per line'''
    return [
'987654321111111',
'811111111111119',
'234234234234278',
'818181911112111']


@pytest.fixture
def parsed():
    '''Expected parser output'''
    return [
'987654321111111',
'811111111111119',
'234234234234278',
'818181911112111']

def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample, parsed):
    assert parse_data(sample) == parsed
