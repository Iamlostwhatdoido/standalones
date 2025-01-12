import numpy as np
import math
import os
import matplotlib.pyplot as plt


clear = lambda: os.system('cls')
clear()

clamp = lambda value, minv, maxv: max(min(value, maxv), minv)

def singleDieSuccessChance(faces, target):
    return clamp((faces+1-target)/faces,0,1)

def multipleDiceSuccessChance(faces, target, dice_number):
    return 1-(1-singleDieSuccessChance(faces,target))**dice_number

def expectedMultipleDiceSuccess(faces, target, dice_number):
    return singleDieSuccessChance(faces,target)*dice_number

def doubleDiceSumChance(faces, target):
    if target < 2 or target > 2*faces:
        return 0
    else:
        return min(target-1,2*faces-target+1)/faces**2

def doubleDiceSuccessChance(faces,target):
    if target > 2*faces:
        return 0
    elif target < 2 :
        return 1
    else:
        out = 0
        for k in range(target, 2*faces+1):
            out += doubleDiceSumChance(faces, k)
        return out


difficulty = [k for k in range(2*10+1)]
d20 = [singleDieSuccessChance(20,k) for k in difficulty]
d10 = [singleDieSuccessChance(10,k) for k in difficulty]
d6 = [singleDieSuccessChance(6,k) for k in difficulty]
sum2d10 = [doubleDiceSuccessChance(10,k) for k in difficulty]
sum2d6 = [doubleDiceSuccessChance(6,k) for k in difficulty]

plt.plot(difficulty,d20)
plt.plot(difficulty,d10)
plt.plot(difficulty,d6)
plt.plot(difficulty,sum2d10)
plt.plot(difficulty,sum2d6)

plt.show()

difficulty = [k for k in range(13)]
TwoD10 = [expectedMultipleDiceSuccess(10,k,2) for k in difficulty]
ThreeD10 = [expectedMultipleDiceSuccess(10,k,3) for k in difficulty]
FourD10 = [expectedMultipleDiceSuccess(10,k,4) for k in difficulty]
FiveD10 = [expectedMultipleDiceSuccess(10,k,5) for k in difficulty]

plt.plot(difficulty,TwoD10)
plt.plot(difficulty,ThreeD10)
plt.plot(difficulty,FourD10)
plt.plot(difficulty,FiveD10)
plt.show()
