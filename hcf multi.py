def smaller_num(*num):
	least=num[0]
	for i in num:
		if i<least:
			least=i
	return least
def hcf(*num):
	a=smaller_num(*num)
	hcf1=a
	for i in range(0,len(num)):
		for j in range(a,0,-1):
			if num[i]%j==0:
				hcf1=j
				break
			else:
				continue
	return hcf1
num=1,3,5
print(hcf(*num))
			
		