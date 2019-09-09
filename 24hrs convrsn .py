time=int(input("Hours: "))
time2=int(input("Mins: "))
time1=input("am/pm: ")
if time1=="am":
	print(time,":",time2,"hrs")
else:
	print(time+12,":",time2,"hrs")