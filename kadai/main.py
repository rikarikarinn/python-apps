import math
import random

aori_list = [
    "え〜！こんなのもわからないの〜？だっさ〜！しょうがないから僕が計算してあげるよ〜（汗汗）",
    "僕に頼るの〜！小学生からやり直した方がいいんじゃない？😅",
    "あれ？計算できないの？もしかして、頭がパンクしちゃったのかな？",
    "計算できないの？もしかして、頭の中がごちゃごちゃなのかな？",
]

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
    rad  = math.radians(deg)
    return math.sin(rad)
    
def cos_deg(deg):
    rad =  math.radians(deg)
    return math.cos(rad)

def tan_deg(deg):
    rad = math.radians(deg)
    return math.tan(rad)


while True:
    print("選択してください")
    print("1. たし算")
    print("2. 引き算")
    print("3. 掛け算")
    print("4. 割り算")
    print("5. 平方根")
    print("6. 余り算")
    print("7. sin")
    print("8. cos")
    print("9. tan")
    print("10. 終了")

    choice = input("選択:")

    if choice == '10':
        print("終了")
        break

    if choice in ('1','2','3','4','6'):
        num1 = float(input("最初の数: "))
        num2 = float(input("次の数: "))
        input(random.choice(aori_list) + "/nEnterで結果出力")

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

    elif choice in ('5','7','8','9'):
        num = float(input("値を入力してください: "))  # 共通して数値入力
        input(random.choice(aori_list) + "/nEnterで結果出力")

        if choice == '5':
            print("√", num, "=", square_root(num))
        elif choice == '7':
            print("sin(", num, ") =", sin_deg(num))
        elif choice == '8':
            print("cos(", num, ") =", cos_deg(num))
        elif choice == '9':
            print("tan(", num, ") =", tan_deg(num))

else:
        print("無効な値です")