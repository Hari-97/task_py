from os.path import *
from datetime import *

obj=datetime.now()

if exists("big"):
	print("hi")
else:
	f=open("big","x")
	
f=open("big","w")
f.write("{}".format(obj))
f=open("big","a")
f.write("\nhello world")
obj1=datetime.now()
f.write("\n{}".format(obj1))
f=open("big","r")

a=(f.read())
print(a)
if a=="{}\nhello world\n{}".format(obj,obj1):
	print("valid")