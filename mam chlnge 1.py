start=int(input("Enter the start value for the range: "))
stop=int(input("Enter the stop value for the range: "))
for i in range(start,stop+1):
	rev=0
	sum=0
	fact=1
	
	print("\n**Num : {}**".format(i))
	cube=i*i*i
	
	for j in range(1,i+1):
		fact=fact*j
		
	while i>0:
		rem=i%10
		rev=rev*10+rem
		sum=sum+rem
		i=i//10
		
	print("Rev  : {}".format(rev))
	print("Sum  : {}".format(sum))
	print("Cube : {}".format(cube))
	print("Fact : {}".format(fact))