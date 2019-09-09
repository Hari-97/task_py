quantity=146
g500=103
kg1=15
kg2=27
kg5=20
avail=[103,15,27,20]
allocs=[0,0,0,0]
allocs1=[0,0,0,0]
post_allocs=[]
	
for i in range(50,g500+1,10):
	allocs1[0]=i
	allocs[0]=i
	if allocs[0]*0.5==quantity:
		break
	else:
		continue
a=allocs[0]*0.5
if a<quantity:
	for i in range(50,kg1+1,10):
		allocs[1]=i
		allocs1[1]=i
		b=allocs[1]*1
		
		if a+b>=quantity:
			if a+b==quantity:
				break
			elif a+b>quantity:
				allocs1[1]=allocs[1]
				allocs[1]=allocs[1]-10
				break

		
c=a+allocs[1]*1
if c<quantity:
	for i in range(50,kg2+1,10):
		allocs[2]=i
		allocs1[2]=i
		d=allocs[2]*2
		
		if c+d>=quantity:
			if c+d==0:
				break
			elif c+d>0:
				allocs1[2]=allocs[2]
				allocs[2]=allocs[2]-10
				if allocs[2]<50:
					allocs[2]==0
				
				break

e=c+allocs[2]*2
if e<quantity:
	for i in range(20,kg5+1,10):
		allocs[3]=i
		allocs1[3]=i
		f=allocs[3]*5
		if e+f>=quantity:
			allocs1[3]=allocs[3]
			allocs[3]=allocs[3]-10

			if allocs[3]<20:
				allocs[3]=0
	
			break
		

sum1=(allocs[0]*0.5+allocs[1]*1+allocs[2]*2+allocs[3]*5)
diff1=quantity-sum1
print(allocs)
print(diff1)

sum2=(allocs1[0]*0.5+allocs1[1]*1+allocs1[2]*2+allocs1[3]*5)
diff2=quantity-sum2
print(allocs1)
print(diff2)

if diff1<0:
	diff1_1=(diff1)*(-1)
else:
	diff1_1=diff1
if diff2<0:
	diff2_2=(diff2)*(-1)
else:
	diff2_2=diff2
	
if diff1_1<diff2_2:
	print("allocation : ",allocs)
	print("reminder : ",diff1)
	post_allocs.extend(allocs)
else:
	print("allocation : ",allocs1)
	print("reminder : ",diff2)
	post_allocs.extend(allocs1)
	
for i in range(0,len(post_allocs)):
	post_allocs[i]=(avail[i])-(post_allocs[i])
print("Post allocation capacity : ", post_allocs)

