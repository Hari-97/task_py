def greater_num(num1,num2):
	if num1>num2:
		return num1
	else:
		return num2
def lcm(num1,num2):
	d=greater_num(num1,num2)
	while True:
		if (d%num1==0) and (d%num2==0):
			return d
			break
		else:
			d+=1
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
a=lcm(num1,num2)
print(a)
		