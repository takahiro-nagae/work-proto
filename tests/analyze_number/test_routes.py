import pytest

PATH = '/analyze_number'


def test_analyze_number_even(client):
    response = client.post(PATH, data={'num': 4})
    assert response.status_code == 200


def test_analyze_number_odd(client):
    response = client.post(PATH, data={'num': 3})
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
