import time 
import math

num = int(input(""))
num2 = int(input(""))

time.sleep(num2/1000)

result = math.sqrt(num)

print(f"Square root of {num} after {num2} milliseconds is {result}")