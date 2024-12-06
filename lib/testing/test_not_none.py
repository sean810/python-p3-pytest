#!/usr/bin/env python3

from lib.not_none_functions import check_not_none


def test_check_not_none():
    # Test case 1: Check if the function returns True for a non-None value
    assert check_not_none("test") == True

    # Test case 2: Check if the function returns False for a None value
    assert check_not_none(None) == False