import time
import random

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




