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
'123 328  51 64',
' 45 64  387 23',
'  6 98  215 314',
'*   +   *   +'
    ]


@pytest.fixture
def parsed():
    '''Expected parser output'''
    return [
        [
        [123, 45, 6],
        [328, 64, 98],
        [51, 387, 215],
        [64, 23, 314]
        ],
        ['*', '+', '*', '+']
    ]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample, parsed):
    assert parse_data(sample) == parsed
