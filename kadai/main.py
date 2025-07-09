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

while True:
    print("選択してください")
    print("1. たし算")
    print("2. 引き算")
    print("3. 掛け算")
    print("4. 割り算")
    print("5. 終了")

    choice = input("選択: ")

    if choice == '5':
        print("終了")
        break

    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("最初の数: "))
            num2 = float(input("次の数: "))
        except ValueError:
            print("数値を入力してください")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1,"*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("無効な選択です")