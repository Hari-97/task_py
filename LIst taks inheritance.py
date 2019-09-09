class Task1:
	lst=[1,1,2,5,5,6,5,9,9,4]
	
	@classmethod
	def maxi(cls):
		cls.maxm=cls.lst[0]
		for i in cls.lst:
			if i >cls.maxm:
				cls.maxm=i
			else:
				continue
		print("The max value is ",cls.maxm)
		
	@classmethod
	def mini(cls):
		cls.minm=cls.lst[0]
		for i in cls.lst:
			if i <cls.minm:
				cls.minm=i
			else:
				continue
		print("The min value is ",cls.minm)
		
class Task2(Task1):
	lst1=[]
	@staticmethod
	def dup():
		for i in Task1.lst:
			if i not in Task2.lst1:
				Task2.lst1.append(i)
			else:
				continue
		print("Duplicates = ",Task2.lst1)
	
	lst2=[]		
	@staticmethod
	def odd():
		count=0
		for i in Task1.lst:
			count+=1
		for i in range(0,count):
			if i%2==0:
				Task2.lst2.append(Task1.lst[i])
		print("odd items = ",Task2.lst2)

class Task3(Task2):
	def pos(self):
		print(self.lst)
		lst.index(self.maxm)
		lst.index(self.minm)
		
		
	def exten(self):
		self.lst3=["a","b","c"]
		print("A = ",self.lst)
		print("B = ",self.lst3)
		print("C = A + B")
		print("C = ",self.lst+self.lst3)
	
class Task4(Task3):
	@classmethod
	def swap(cls):
		lst_1=[]
		print("Before swapping = ",cls.lst)
		x=cls.lst[-1]
		y=cls.lst[1:-1]
		z=cls.lst[0]
		lst_1.append(x)
		lst_1.extend(y)
		lst_1.append(z)
		print("After swapping = ",lst_1)
		
	@staticmethod
	def merg_sort():
		lst4=[2,3,8]
		lst_2=Task1.lst+lst4
		lst_2.sort()
		print(lst_2)
		
		
	def ind(self):
		print("Given list = ",self.lst)
		a=int(input("Enter an element to find index : "))
		if a in self.lst:
			print(" index of {} = ".format(a),self.lst.index(a))
		else:
			print("No such element found")
		
lst=[1,1,2,5,5,6,5,9,9,4]		
List=Task4()
print("Max and Min: ")
Task4.maxi()
Task4.mini()
print("\nDuplicates in a list:")
Task4.dup()
print("\nOdd elements:")
Task4.odd()
print("\nPosition of max,min:")
Task4.pos(Task1)
print("\nExtend without append:")
Task4.exten(Task2)
print("\nSwapping 1st and last elemnts:")
Task4.swap()
print("\nMerge and sort:")
Task4.merg_sort()
print("\nIndex:")
Task4.ind(Task3)
		
		
		
	
				
				
		
		
	
		