class Atm:
	
	def __init__(self,cur_bal):
		self.cur_bal=cur_bal
		
	def deposit(self):
		while True:
			try:
				self.dep=int(input("\nEnter the amount to be deposited : "))
				break
			except:
				print("Enter the amount in numerals\n")
		
		self.cur_bal=self.cur_bal+self.dep
		
		enter=input("Press ENTER to deposit your amount")
		print("Your amount has been deposited succesfully!")
		print("Your current balance is {}".format(self.cur_bal))
		
	def withdrawal(self):
		while True:
			try:
				self.withdraw=int(input("\nEnter the amount to be withdrawn : "))
				break
			except:
				print("Enter the amount in numerals\n")
		
		self.cur_bal=self.cur_bal-self.withdraw
		
		print("Please collect your cash!")
		print("Your current balance is {}".format(self.cur_bal))
		
	def bal_enquiry(self):
		print("\nYour current balance is {}".format(self.cur_bal))
		
	def exit(self):
		print("\nThank You! Visit Again!")

transaction=Atm(5000)

print("\tWelcome to the Atm!\n1.Deposit\n2.Withdrawal\n3.Balance enquiry\n4.Exit")

swipe=input("\nPlease SWIPE your card to begin the transaction")

while True:
	while True:
		try:
			pin=int(input("\nEnter the pin: "))
			break
		except:
			print("Only numerals allowed")
			
	if pin==1234:
		break
	else:
		print("Invalid pin")
		
while True:
	while True:
		try:
			choice=int(input("\nSelect the operation : "))
			break
		except:
			print("only numerals will be accepted")
		
	if choice==1:
		transaction.deposit()
	elif choice==2:
		transaction.withdrawal()
	elif choice==3:
		transaction.bal_enquiry()
	elif choice==4:
		transaction.exit()
		break
	else:
		print("Invalid operation")
			
		
	
		