from threading import *
from time import *

class Tickets:
	#Reservation of movie tickets
	
	def __init__(self,available,scrn):
		#initialisation of arguments
		self.available=available
		self.scrn=scrn
		self.lck=Lock()
	
	def reserve(self):
		"""
		param:none
	    return:none
  	 #to reserve tickets for the user
	
	    """
		self.lck.acquire()
		print("\nWelcome to SPI cinemas!\n")
		sleep(1)
		name=current_thread().getName()#gets the threadname
		
		wanted=int(input("Enter the no. of ticket(s) : "))#gets the no.of tickets
		
		if self.available >= wanted:
			
			print("\n SPI cinemas")
			#to print the ticket screen
			for i in self.scrn:
				for j in i:
					print(j,end=" ")
				print()
				
			for i in range(1,wanted+1):
				#to make the user select the tickets
				while True:
					slct=input("Enter  the seat(s): ")
					#to replace the booked ticket with "X" mark 
					if slct in self.scrn[0]:
						self.scrn[0][(self.scrn[0].index(slct))]="X "
						break
					elif slct in self.scrn[1]:
						self.scrn[1][(self.scrn[1].index(slct))]="X "
						break
					elif slct in self.scrn[2]:
						self.scrn[2][(self.scrn[2].index(slct))]="X "
						break
					elif slct in self.scrn[3]:
						self.scrn[3][(self.scrn[3].index(slct))]="X "
						break
					elif slct in self.scrn[4]:
						self.scrn[4][(self.scrn[4].index(slct))]="X "
						break
					else:
						print("Please Enter the available seat")
						continue
						
			print("\n SPI cinemas")
			#prints the ticket screen after booking
			for i in self.scrn:
				for j in i:
					print(j,end=" ")
				print()
		
			print("\n{} seat(s) have been confirmed to {}".format(wanted,name))
			self.available-=wanted
		else:
			print("Sorry! {} ,Only {} seats available".format(name,self.available))
		
		sleep(2)
		self.lck.release()

scrn=[["A1","A2","A3","A4","A5"],["B1","B2","B3","B4","B5"],["C1","C2","C3","C4","C5"],["D1","D2","D3","D4","D5"],["E1","E2","E3","E4","E5"],["  <Screen>     "]]
			
Booking=Tickets(25,scrn)

t1=Thread(target=Booking.reserve)
t2=Thread(target=Booking.reserve)
t3=Thread(target=Booking.reserve)

t1.setName("Hari")
t2.setName("Pradeep")
t3.setName("Faizal")

t1.start()
t2.start()
t3.start()

		