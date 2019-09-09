bagcp=8
bag=[]
things=["guide","laptop","mobile","dress","books","waterbottle","box"]

value={500:"guide",40000:"laptop",20000:"mobile",2000:"dress",450:"books",200:"waterbottle",150:"box"}

weight={"guide":2,"laptop":5,"mobile":1,"dress":3,"books":3,"waterbottle":0.5,"box":0.5}

value1=list(value.keys())
value1.sort()

i=len(value1)-1
j=0

while i>=0:
	w=value.get(value1[i])
	bag.append(weight.get(w))
	
	if sum(bag)>=bagcp:
		diff=sum(bag)-bagcp
		
		if diff>0:
			bag.pop()
			
			if sum(bag)<bagcp:
				i-=1
				j+=1
				continue
			else:
				break
	i-=1
	j+=1
	
a=list(weight.keys())
b=list(weight.values())


bag1=[]
for i in bag:
	if i in b:
		bag1.append(a[b.index(i)])
		
print("The available items are :\n",",".join(things))

print("\nvalues of each item :\n",value)

print("\n weight of each item:\n",weight)

print("\nbag capacity: ",bagcp)
		
print("\nThe bag can hold :\n",",".join(bag1))
	




		

