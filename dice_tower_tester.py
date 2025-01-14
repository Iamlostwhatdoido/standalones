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

tries = int(input("Number of tries (0 means it will keep going until "" is inputted) : "))
if tries == 0 : tries = -1
previous_rolls = 1
print("Start with face '1' up")

i=1
while tries != 0:
	result = input('('+str(i)+") result : ")
	if result == "" : break
	result_matrix[previous_rolls-1,int(result)-1] +=1
	previous_rolls = int(result)

	i+=1
	tries -=1

print(result_matrix)