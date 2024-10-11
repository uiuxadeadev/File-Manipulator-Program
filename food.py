# food.py
# import sys

# # 食べ物を尋ねるメッセージを標準出力に書き込む
# sys.stdout.buffer.write(b'What is your favorite food?\n')
# sys.stdout.flush()

# # 標準入力から回答を読み込む
# food = sys.stdin.buffer.readline().decode().strip()  # デコードとトリミング
# print('Thanks for letting me know your favorite food is ' + food)


# food = input('What is your favorite food??\n')
# print('Thanks for letting me know your favorite food is ' + food)

# food.py
import sys

# 食べ物を尋ねるメッセージを表示
sys.stdout.write('What is your favorite food?\n')
sys.stdout.flush()  
# 標準入力からの応答を取得
food = sys.stdin.readline().strip()

# 応答を出力
print('Thanks for letting me know your favorite food is ' + food)
