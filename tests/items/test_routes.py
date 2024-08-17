import pytest

PATH = '/items'


def test_stock_list(client):
    response = client.get(PATH)

    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
