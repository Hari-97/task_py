row=int(input("Enter the rows: "))
for i in range(1,row+1):
	if i==1:
		for j in range(1,2):
			print("*")
	else:
		for j in range(1,row+1-i):
			print(end=" ")
		for j in range(1,i):
			print("*",end="")
		for j in range(1,i):
			print("*",end="")
	print()