row=3
for i in range(1,2*row):
	for j in range(1,2*row):
		if (i==1) or (i==2*row-1) or ((j==1 or j==2*row-1) and (i>1 and i<2*row-1)):
			print(row,end=" ")
		elif(i==3 and j==3):
			print(1,end=" ")
		else:
			print(row-1,end=" ")
	print()
			