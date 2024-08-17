import pytest


def test_stock_list(client):
    response = client.get('/items')

    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
