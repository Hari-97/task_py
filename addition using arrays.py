a=[2,3,4,6,7]
b=[4,7,9,1,2,3]
if len(a)>len(b):
	diff=len(a)-len(b)
	for i in range(diff):
		b.insert(0,0)
elif len(a)<len(b):
	diff=len(b)-len(a)
	for i in range(diff):
		a.insert(0,0)
c=[]
sum=0
rem=0
i=len(a)-1
while i>=0:
	sum=rem+a[i]+b[i]
	rem=0
	sum1=str(sum)
	if len(sum1)==2:
		c.append(int(sum1[-1]))
		rem=int(sum1[0])
	else:
		c.append(sum)
	i-=1
c.reverse()
for i in c:
	print(i,end="")
		