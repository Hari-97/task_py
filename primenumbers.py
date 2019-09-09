from try1 import *

class Primeornot(Sumofdigits):
    def findingprimenum(self):
        self.prime1=[]
        self.nonprime1=[]
        for i in self.list_of_sum:
            count=0
            for j in range(i,0,-1):
                if i%j==0:
                    count+=1
            if i==1 or count==2:
                self.prime1.append(i)
            else:
                self.nonprime1.append(i)
    

