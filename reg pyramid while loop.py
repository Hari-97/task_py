row=4
i=1
while i<=row:
	print(" "*(row-i),end="")
	if i==1:
		print("*",end="")
	else:
		print("*"*(i+(i-1)),end="")
	i+=1
	print()
	continue
