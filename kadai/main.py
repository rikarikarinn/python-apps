import math
import random

# あおり文句リスト
aori_list = [
    "え〜！こんなのもわからないの〜？だっさ〜！しょうがないから僕が計算してあげるよ〜（汗汗）",
    "僕に頼るの〜！小学生からやり直した方がいいんじゃない？😅",
    "あれ？計算できないの？もしかして、頭がパンクしちゃったのかな？",
    "計算できないの？もしかして、頭の中がごちゃごちゃなのかな？",
]

# 各種関数定義
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: 負の数の平方根は計算できません"

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: 0で割ることはできません"

def sin_deg(deg):
    return math.sin(math.radians(deg))

def cos_deg(deg):
    return math.cos(math.radians(deg))

def tan_deg(deg):
    return math.tan(math.radians(deg))

# 計算機モード
def calculator():
    while True:
        print("\n[計算機モード]")
        print("1. たし算  2. 引き算  3. 掛け算  4. 割り算  5. 平方根  6. 余り算")
        print("7. sin  8. cos  9. tan  0. 終了")
        choice = input("選択:")
        if choice == '0':
            print("計算機を終了します。ゲームに戻ります。\n")
            break

        if choice in ('1','2','3','4','6'):
            try:
                num1 = float(input("最初の数: "))
                num2 = float(input("次の数: "))
                print(random.choice(aori_list))
                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))
                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))
                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))
                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                elif choice == '6':
                    print(num1, "%", num2, "=", modulus(num1, num2))
            except:
                print("無効な数値です。")

        elif choice in ('5','7','8','9'):
            try:
                num = float(input("値を入力してください: "))
                print(random.choice(aori_list))
                if choice == '5':
                    print("√", num, "=", square_root(num))
                elif choice == '7':
                    print("sin(", num, ") =", sin_deg(num))
                elif choice == '8':
                    print("cos(", num, ") =", cos_deg(num))
                elif choice == '9':
                    print("tan(", num, ") =", tan_deg(num))
            except:
                print("無効な数値です。")
        else:
            print("無効な選択です。")

# クイズ問題生成
def generate_problem():
    ops = ['+', '-', '*', '/']
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    op = random.choice(ops)
    if op == '/':
        y = random.randint(1, 10)
        question = f"{x * y} / {y}"
        answer = x * y / y
    else:
        question = f"{x} {op} {y}"
        answer = eval(question)
    return question, answer

# クイズモード
def quiz_game():
    score = 0
    for i in range(5):
        q, a = generate_problem()
        print(f"\n問題{i+1}: {q} = ?")
        print("答えるには数字を入力してください。計算機を使うなら 'c' を入力してください。")
        user_input = input("答え or 'c': ").strip()
        if user_input.lower() == 'c':
            calculator()
            user_input = input("再度答えを入力してください: ")

        try:
            user_answer = float(user_input)
            if abs(user_answer - a) < 1e-6:
                print("正解！")
                score += 1
            else:
                print(f"不正解！正解は {a} です")
        except:
            print("無効な入力です。")
    print(f"\nゲーム終了！あなたのスコアは {score} / 5 でした\n")

# メインメニュー
while True:
    print("選択してください")
    print("1. 計算機")
    print("2. クイズ")
    print("3. 終了")

    choice = input("選択: ")

    if choice == '1':
        calculator()
    elif choice == '2':
        quiz_game()
    elif choice == '3':
        print("終了します。")
        break
    else:
        print("無効な選択です。")
