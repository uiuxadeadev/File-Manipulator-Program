"""
markdown_converter.py

このスクリプトは、MarkdownファイルをHTMLに変換するためのツールです。
コマンドラインからファイルを指定して、Markdown形式のテキストをHTML形式に変換し、出力ファイルに保存します。

使い方:
    python3 markdown_converter.py markdown inputfile outputfile

引数:
    markdown: 実行するコマンド（固定）
    inputfile: 変換するMarkdownファイル（例: example.md）
    outputfile: 変換後のHTMLファイルの保存先（例: example.html）

例:
    python3 markdown_converter.py markdown example.md example.html

要件:
    - Python 3
    - markdownライブラリ (インストールするには `pip install markdown` を実行)

エラーハンドリング:
    - 入力ファイルが存在しない場合、ファイルが見つからないエラーメッセージが表示されます。
    - コマンドライン引数が不正の場合、正しい使用方法が表示されます。
"""


import sys
import markdown
import os

def convert_markdown_to_html(input_file, output_file):
    try:
        # 入力ファイルを開いてMarkdownを読み込み
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_text = f.read()

        # MarkdownをHTMLに変換
        html_text = markdown.markdown(markdown_text)

        # 出力ファイルにHTMLを書き込み
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_text)

        print(f"変換完了: {output_file} にHTMLを保存しました。")
    except FileNotFoundError:
        print(f"エラー: ファイル {input_file} が見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    # コマンドライン引数を取得
    if len(sys.argv) != 4 or sys.argv[1] != "markdown":
        print("Usage: python3 markdown_converter.py markdown inputfile outputfile")
    else:
        input_file = sys.argv[2]
        output_file = sys.argv[3]

        # 入力ファイルが.md拡張子かを確認
        if not input_file.endswith(".md"):
            print("エラー: 入力ファイルは.mdファイルである必要があります。")
        else:
            convert_markdown_to_html(input_file, output_file)
