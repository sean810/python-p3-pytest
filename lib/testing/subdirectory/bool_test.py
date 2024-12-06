#!/usr/bin/env python3

from lib.bool_functions import return_true


def test_return_true():
    '''in bool_functions, function "return_true" returns True.'''
    assert return_true() == True
