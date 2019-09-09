class String:
	def __init__(self,str1):
		self.str1=str1
	def get_string(self):
		str1=input("Enter a string : ")
		return str1
	def print_string(self):
		print(str1.upper())
str1=""
obj=String(str1)
str1=String.get_string(str1)
String.print_string(str1)
	