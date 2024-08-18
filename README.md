# work_proto
ルーティングとhtmlのレンダリングを簡易にするためFlask とjinjaを採用した。

クローン後以下を実行し、依存関係をインストール
pythonのバージョンによって適宜python3 or pip3に読み替える。
```
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```

app.pyを実行すればローカル環境が立ち上がる。

# ディレクトリ構成

```
/
├── analyze_number/ 数値の解析：偶数奇数/素数
    ├── templates/ ページのテンプレート
    ├── logic.py   各種ロジック
    ├──  routes.py ルーティング
├── error/ エラーハンドラ
├── items/ 在庫一覧
├── template_filter/ テンプレートから参照するカスタムフィルター
├── templates/ トップページ/汎用パーツ/エラーページなど
├── tests/ 各種テスト
```
