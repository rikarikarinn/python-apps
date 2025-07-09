import time
import random

def reaction_test():
    t = random.uniform(5,15)
    time.sleep(t)

    print("押す")

    start_time = time.time()
    input()
    end_time = time.time()
 

    re_time = end_time - start_time

    if re_time < 0.01:
        print("早すぎます")
    else:
        print(f"速度は{re_time:.4f}秒")   


def ask_yes_no(prompt="もう一回やりますか？"):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes"):
            return True
        if answer in ("no"):
            return False
        print("入力が無効ですYesかNOで答えてください")
    
def main():
    while True:
        reaction_test()
        if not ask_yes_no():
            print("さようなら")
            break
if __name__ == "__main__":
    main()