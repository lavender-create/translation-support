
# Translation Support App

Flask と OpenAI API を使った、業務向けの翻訳サポートアプリです。  
日本語・英語の文章を入力すると、翻訳・要約・意図解析をまとめて確認できます。  
ブラウザの音声入力（日本語 / 英語）にも対応しています。

---

## 主な機能
- 日本語 ⇄ 英語の翻訳
- 翻訳結果の要約
- 意図解析（Question / Request / Information など）
- 音声入力対応（Chrome / Edge）

---

## 技術スタック
- Python
- Flask
- OpenAI API
- HTML / CSS / JavaScript
- Web Speech API（音声入力）

---

## セットアップについて

本アプリはローカル環境での利用を想定しています。  
必要なライブラリは以下のコマンドでインストールします。

```bash
pip install -r requirements.txt

## 補足
- OpenAI APIキーは `.env` ファイルで管理します
- `.env` は GitHub には含めていません
- 音声入力は Chrome / Edge を推奨します






