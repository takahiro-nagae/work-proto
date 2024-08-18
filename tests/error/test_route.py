def test_404_error(client):
    # 存在しないページにアクセス
    response = client.get('/nonexistent-page')
    assert response.status_code == 404
    assert "ページが見つかりません" in response.get_data(as_text=True)