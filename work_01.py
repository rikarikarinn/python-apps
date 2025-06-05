import random
i = 0
random_n = random.randint(1,100)
#random_n = 3
for i in range(5):
    input_line = int(input("1~100までの数"))
    print("入力された値", input_line)
    if random_n == int(input_line):
        print("正解")
        break
    else:
        print("不正解")
        if input_line < random_n:
            if random_n - input_line > 10:
                print("10以上大きい")
            else:
                print("もっと大きい数字ですがだいぶ近い")
        else:
            if input_line - random_n > 10:
                print("10以上小さい")
            else:
                print("もっと小さい数字ですがだいぶ近い")

print("正解の値",random_n)
