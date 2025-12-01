'''
Unit tests
'''

import pytest

# TODO: Change from skel to current day
from skel import *

from . import __main__ as tmain


@pytest.fixture
def sample():
    return ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

@pytest.fixture
def parsed():
    return [('L', 68), ('L', 30), ('R', 48), ('L', 5), ('R', 60), ('L', 55),
            ('L', 1), ('L', 99), ('R', 14), ('L', 82)]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample, parsed):
    assert parse_data(sample) == parsed
