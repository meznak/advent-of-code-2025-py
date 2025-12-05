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
'3-5',
'10-14',
'16-20',
'12-18',
'',
'1',
'5',
'8',
'11',
'17',
'32'
    ]


@pytest.fixture
def parsed():
    '''Expected parser output'''
    return [
        [
            [3, 5],
            [10, 14],
            [16, 20],
            [12, 18]
        ],
        [
            1, 5, 8, 11, 17, 32
        ]
    ]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample: list[str], parsed: list):
    assert parse_data(sample) == parsed
