class Tuple:
	
	def __init__(self,str1):
		self.str1=str1
		
		
	def string_conv(self):
		
		self.str2="".join(self.str1)
		
		print("The converted string is ",self.str2)
		
		
	def ele_4(self):
		
		print("4th element : ",self.str2[4])
		
		print("4th element from last : ",self.str2[-4])
		
		
	def exist(self):
		
		check=input("Enter the element to check : ")
		
		if check in self.str2:
			
			print("{} exists".format(check))
			
		else:
			
			print("{} does not exist".format(check))
			
			
	def remov(self):
		
		element=input("Enter the element to remove : ")
		
		if element in self.str2:
			
			b=list(self.str2)
			
			b.remove(element)
			
			print("The element {} has been removed".format(element))
			
			print(tuple(b))
			
		else:
			
			print("The element does not exist")
			
			
	def rev(self):
		
		c=list(self.str2)
		
		c.reverse()	
			
		print("Reverse : ",tuple(c))


str1=("c","h","e","n","n","a","i")

obj=Tuple(str1)

print("\tString conversion")
obj.string_conv()

print("\n\tFinding the 4th element")
obj.ele_4()

print("\n\tCheck existence")
obj.exist()

print("\n\tRemoving element")
obj.remov()

print("\n\tReversing the tuple")
obj.rev()

		