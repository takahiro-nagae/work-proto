import pytest

from analyze_number.analyze_number import is_even


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-3) is False


if __name__ == '__main__':
    pytest.main()
