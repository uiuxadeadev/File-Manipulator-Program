"""
プログラムの説明
1. 入力の検証:
ユーザーに最小値（n）と最大値（m）を入力してもらいます。
n が m より大きい場合は再入力を促します。
無効な入力（数字以外）も処理します。

2. 乱数の生成:
random.randint(n, m) を使用して、指定された範囲内で乱数を生成します。

3. ゲームループ:
ユーザーは最大5回の試行で乱数を推測します。
各推測に対して、ユーザーにフィードバックを提供します（大きい/小さい/正解）。

4. 試行回数の制限:
ユーザーが指定された試行回数を超えた場合、生成された乱数を表示します。
"""

import random

def main():
    # 最小値と最大値の入力
    while True:
        try:
            n = int(input('最小数を入力してください (n): '))
            m = int(input('最大数を入力してください (m): '))
            if n > m:
                print("最小数は最大数以下でなければなりません。再度入力してください。")
            else:
                break
        except ValueError:
            print("無効な入力です。数字を入力してください。")

    # 乱数の生成
    random_number = random.randint(n, m)
    print(f'{n} から {m} の範囲で乱数を生成しました。')

    # 最大試行回数の設定
    max_attempts = 5
    attempts = 0

    # ゲームループ
    while attempts < max_attempts:
        try:
            guess = int(input(f'乱数を推測してください (試行回数 {attempts + 1}/{max_attempts}): '))
            attempts += 1

            if guess < n or guess > m:
                print(f"推測は {n} から {m} の範囲内でなければなりません。")
                continue

            if guess < random_number:
                print("もっと大きいです。")
            elif guess > random_number:
                print("もっと小さいです。")
            else:
                print(f'正解です！ 生成された乱数は {random_number} でした。')
                break

        except ValueError:
            print("無効な入力です。数字を入力してください。")

    if attempts == max_attempts:
        print(f'試行回数を超えました。生成された乱数は {random_number} でした。')

if __name__ == '__main__':
    main()
