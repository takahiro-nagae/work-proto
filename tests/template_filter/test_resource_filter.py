import pytest

from template_filter.resource_filter import bool_to_symbol


def test_bool_to_symbol():
    assert bool_to_symbol(True) == '○'
    assert bool_to_symbol(False) == '×'
    assert bool_to_symbol('a') == 'a'


if __name__ == '__main__':
    pytest.main()
