"""
Helps with timing and comparing functions speed
"""


import time
import numpy as np

def timer(func):
    def wrapper(*arg1,**arg2):
        start_time = time.time()
        out = func(*arg1,**arg2) 
        end_time = time.time() - start_time
        print(f'The function took {end_time} seconds')
        return out
    return wrapper

@timer
def method1(n):
    out = np.log(float(n))/np.log(3)
    return out

@timer
def method2(n):
    num = float(n)
    i = 0
    while num > 1:
        num = num/3.0
        i += 1
    return i



n = 3**4 + 1

a = method1(n)
b = method2(n)
print(a,b)