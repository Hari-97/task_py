user_count=0
comp_count=0
from random import *

def comp():
	if op==1:
		return ("stone")
	elif op==2:
		return ("paper")
	elif op==3:
		return ("scissor")
def stone():
	global user_count
	global comp_count
	if op==1:
		return "\nResult : null :|"
	elif op==2:
		comp_count+=1
		return "\nResult : you lose :("
	elif op==3:
		user_count+=1
		return "\nResult : you win ;)"
def paper():
	global user_count
	global comp_count
	if op==1:
		user_count+=1
		return "\nResult : you win ;)"
	elif op==2:
		return "\nResult : null :|"
	elif op==3:
		comp_count+=1
		return "\nResult : you lose :("
def scissor():
	global user_count
	global comp_count
	if op==1:
		comp_count+=1
		return "\nResult : you lose :("
	elif op==2:
		user_count+=1
		return "\nResult : you win ;)"
	elif op==3:
		return "\nResult : null :|"
while True:
	op=(randint(1,3))
	user=input("  You   : ")
	print("Computer: ",end="")
	print(comp())
	if user=="stone":
		print(stone())
	elif user=="paper":
		print(paper())
	elif user=="scissor":
		print(scissor())	
	print("\nYour Points : {}".format(user_count),end=" ")
	print("\tComputer Points : {} \n\n".format(comp_count))
	if user_count==10 or comp_count==10:
		if user_count==10:
			print("Congratulations on your victory!")
			break
		else:
			print("Sorry for you loss!")
			break



		

