import pytest

PATH = '/analyze_number'


def test_analyze_number_even(client):
    response = client.post(PATH, data={'num': 4})
    assert response.status_code == 200


def test_analyze_number_odd(client):
    response = client.post(PATH, data={'num': 3})
    assert response.status_code == 200


def test_analyze_number_none(client):
    response = client.post(PATH, data={'num': ''})
    assert response.status_code == 400
    assert '数値を入力してください' in response.get_data(as_text=True)


def test_analyze_not_number_none(client):
    response = client.post(PATH, data={'num': 'aaa'})
    assert response.status_code == 400
    assert '有効な数値を入力してください' in response.get_data(as_text=True)


if __name__ == '__main__':
    pytest.main()
