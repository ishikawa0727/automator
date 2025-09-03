# Automator

## 概要

このプロジェクトには2つのPythonスクリプトが含まれています。

1. GUI操作自動化ツール

2. 画像PDF化ツール

---

## 2. GUI操作自動化ツール

### 機能

* JSON形式の設定ファイルを読み込み、指定されたアクションを順に実行
* サポートアクション:

  * `loop` : 指定回数シーケンスを繰り返す
  * `screenshot` : 指定座標とサイズでスクリーンショットを保存
  * `keyDown` : キー入力をシミュレート
  * `click` : 指定座標でマウスクリック
  * `sleep` : 指定秒数待機

### 使い方

```bash
make start
```

### JSON設定ファイル例

```json
{
  "sequence": [
    {
      "action": "loop",
      "count": 10,
      "sequence": [
        {
          "action": "screenshot",
          "left": 50,
          "top": 50,
          "width": 100,
          "height": 100,
          "start_index": 0,
          "filename": "./images/screenshot-{000}.png"
        },
        {
          "action": "keyDown",
          "key": "left"
        },
        {
          "action": "sleep",
          "time": 1
        }
      ]
    }
  ]
}
```

---

## 1. 画像PDF化ツール

### 機能

* 指定フォルダ内の画像を取得
* ファイル名順に並べる
* PDFに変換し1ページに1画像で出力

### 使い方

```bash
make pdf
```

---

## 依存解決

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# 仮想環境無効化
deactivate
```

### 注意点

* macOSではスクリーンショットやキーボード操作にアクセシビリティ権限が必要です。
* 仮想環境内でインストールして実行することを推奨します。


