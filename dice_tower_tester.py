"""
Jolan ARNAUD
Executable with input/output in terminal
Tests the repartition of roll result through a dice tower.
First roll is made with face 1 upward.
Result is inputted, subsequent rolls are made with previous result face up.
Final matrix shows rolls repartition.
Ideally all matrix cells should be the same.

"""


import numpy as np

dice_size = int(input("Dice size : "))

result_matrix = np.zeros((dice_size,dice_size),int)

tries = 200
previous_rolls = 1

for i in range(tries):
	result = int(input('('+str(i)+") result : "))
	result_matrix[previous_rolls-1,result-1] +=1
	previous_rolls = result

print(result_matrix)