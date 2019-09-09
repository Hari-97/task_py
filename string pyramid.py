str1=input("enter the string")
row=len(str1)
for i in range(0,row+1):
	for j in range(0,i):
		print(str1[j],end="")
	print()