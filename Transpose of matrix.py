a=[1,2,3,4],[5,6,7,8]
row=len(a)
col=len(a[0])
for i in range(0,col):
	for j in range(0,2):
		print(a[j][i],end=" ")
	print()