import pytest

from items.logic import build_dict_for_list


def test_build_dict_for_list():
    data = [
        {
            'id': 1,
            'value': 'aaa'
        },
        {
            'id': 2,
            'value': 'bbb'
        }
    ]

    result = build_dict_for_list(data, 'id', 'value')

    assert result.get(1) == 'aaa'
    assert result.get(2) == 'bbb'


if __name__ == '__main__':
    pytest.main()
