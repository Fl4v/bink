import pytest
from utils import read_csv, sorted_list


def test_sorted_list():

    #Given
    data = sorted_list(read_csv(), 'Current Rent')

    #Then
    assert type(data) == list
    assert all(isinstance(item, float) for item in data)
