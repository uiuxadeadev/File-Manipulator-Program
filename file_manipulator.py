"""
ファイル操作スクリプト (file_manipulator.py)

このスクリプトは、テキストファイルに対する様々な操作を行うためのコマンドラインツールです。
以下の機能を提供します：

1. ファイルの内容を逆順にする
2. ファイルをコピーする
3. ファイルの内容を指定回数複製する
4. ファイル内の特定の文字列を別の文字列に置換する

使用方法:
    python file_manipulator.py <command> <args>

各コマンドの詳細な使用方法については、引数なしでスクリプトを実行すると表示されます。

このスクリプトは、ファイル操作の基本的なタスクを簡単に実行できるようにすることを目的としています。
エラー処理とユーザーフレンドリーなインターフェースを備えており、コマンドラインから簡単に使用できます。
"""

import sys
import os

# ファイルの内容を逆順にする関数
def reverse_file(input_path, output_path):
    with open(input_path, 'r') as input_file:
        content = input_file.read()
    
    # 文字列を逆順にして新しいファイルに書き込む
    with open(output_path, 'w') as output_file:
        output_file.write(content[::-1])

# ファイルをコピーする関数
def copy_file(input_path, output_path):
    with open(input_path, 'r') as input_file:
        content = input_file.read()
    
    # 内容をそのまま新しいファイルに書き込む
    with open(output_path, 'w') as output_file:
        output_file.write(content)

# ファイルの内容を指定回数だけ複製する関数
def duplicate_contents(input_path, n):
    with open(input_path, 'r') as input_file:
        content = input_file.read()
    
    # 内容を n 回複製
    duplicated_content = content * n
    
    # 複製した内容を元のファイルに上書き
    with open(input_path, 'w') as input_file:
        input_file.write(duplicated_content)

# ファイル内の特定の文字列を置換する関数
def replace_string(input_path, needle, newstring):
    with open(input_path, 'r') as input_file:
        content = input_file.read()
    
    # needle を newstring に置換
    updated_content = content.replace(needle, newstring)
    
    # 更新した内容をファイルに書き込む
    with open(input_path, 'w') as input_file:
        input_file.write(updated_content)

# ファイルパスの存在を確認する関数
def validate_file_path(file_path):
    if not os.path.exists(file_path):
        raise ValueError(f"ファイルが存在しません: {file_path}")

# 正の整数であることを確認する関数
def validate_positive_integer(n):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("正の整数を入力してください")
    return n

# 使用方法と利用可能なコマンドを表示する関数
def print_usage():
    print("使用方法: python file_manipulator.py <command> <args>")
    print("\n利用可能なコマンド:")
    print("  reverse <inputpath> <outputpath>")
    print("    inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。")
    print("  copy <inputpath> <outputpath>")
    print("    inputpath にあるファイルのコピーを作成し、outputpath として保存します。")
    print("  duplicate-contents <inputpath> <n>")
    print("    inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。")
    print("  replace-string <inputpath> <needle> <newstring>")
    print("    inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。")

# メイン関数：コマンドライン引数を解析し、適切な関数を呼び出す
def main():
    # コマンドライン引数が不足している場合、使用方法を表示して終了
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1]

    try:
        if command == "reverse":
            if len(sys.argv) != 4:
                raise ValueError("reverse コマンドは2つの引数が必要です")
            input_path, output_path = sys.argv[2], sys.argv[3]
            validate_file_path(input_path)
            reverse_file(input_path, output_path)

        elif command == "copy":
            if len(sys.argv) != 4:
                raise ValueError("copy コマンドは2つの引数が必要です")
            input_path, output_path = sys.argv[2], sys.argv[3]
            validate_file_path(input_path)
            copy_file(input_path, output_path)

        elif command == "duplicate-contents":
            if len(sys.argv) != 4:
                raise ValueError("duplicate-contents コマンドは2つの引数が必要です")
            input_path, n = sys.argv[2], sys.argv[3]
            validate_file_path(input_path)
            n = validate_positive_integer(n)
            duplicate_contents(input_path, n)

        elif command == "replace-string":
            if len(sys.argv) != 5:
                raise ValueError("replace-string コマンドは3つの引数が必要です")
            input_path, needle, newstring = sys.argv[2], sys.argv[3], sys.argv[4]
            validate_file_path(input_path)
            replace_string(input_path, needle, newstring)

        else:
            raise ValueError(f"不明なコマンドです: {command}")

        print("操作が正常に完了しました。")

    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        print("\n使用方法を確認するには、引数なしでスクリプトを実行してください。")
        sys.exit(1)

# スクリプトが直接実行された場合にのみ main() を呼び出す
if __name__ == "__main__":
    main()