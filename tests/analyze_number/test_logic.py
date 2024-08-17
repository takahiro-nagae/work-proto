import pytest

from analyze_number.logic import is_even, is_prime


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-3) is False


def test_is_prime():
    assert is_prime(-1) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(47) is True
    assert is_prime(91) is False
    assert is_prime(1399) is True


if __name__ == '__main__':
    pytest.main()
