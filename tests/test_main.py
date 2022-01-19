import pytest

from attcert.main import read_csv, make_registry


def test_read_csv():
    res = read_csv("test_attendees.csv")

    assert len(res) == 2
    assert res[0][0] == "John Doe"
    assert res[0][1] == "abcd1234"


def test_make_registry():
    res = make_registry([("A", "123"), ("B", "456")])

    assert res == {"123": "A", "456": "B"}


def test_make_registry_duplicated_code():
    with pytest.raises(ValueError):
        make_registry([("A", "123"), ("B", "456"), ("C", "456")])
