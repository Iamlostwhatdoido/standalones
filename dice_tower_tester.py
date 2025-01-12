import numpy as np

dice_size = int(input("Dice size : "))

mat = np.zeros((dice_size,dice_size),int)

tries = 200
previous = 1

for i in range(tries):
	result = int(input('('+str(i)+") result : "))
	mat[previous-1,result-1] +=1
	previous = result

print(mat)