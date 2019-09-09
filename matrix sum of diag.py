x=[1,2,3,4,5,6,7,8,9,10,11]
y=[]
row=int(input("Enter no.of rows: "))
col=int(input("Enter no. of cols: "))
for i in range(0,row):
	y.append([])
for i in range(0,row):
	for j in range(0,col):
		y[i].append(j)

for i in range(0,row):
	for j in range(0,col):
		y[i][j]=int(input())
print(y)

x=[]
for i in range(0,row):
	x.append([])
for i in range(0,row):
	for j in range(0,col):
		x[i].append(j)
for i in range(0,row):
	for j in range(0,col):
		x[i][j]=y[i][j]+1
print(x)

z=[]
for i in range(0,row):
	z.append([])
for i in range(0,row):
	for j in range(0,col):
		z[i].append(j)
for i in range(0,row):		
	for j in range(0,col):
		z[i][j]=x[i][j]+1
print(z)

	
a=1
b=1
c=1	
for i in range(0,row):
	for j in range(0,col):
		if i==j:
			a=a*y[i][j]
			b=b*x[i][j]
			c=c*z[i][j]
			
print("{} + {} + {} = ".format(a,b,c),a+b+c)
