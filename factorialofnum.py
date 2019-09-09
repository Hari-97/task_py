from primenumbers import *

class Factorials(Primeornot):
    def findingfact(self):
        self.list_of_fact=[]
        for i in self.prime1:
            fact=1
            for j in range(i,0,-1):
                fact=fact*j
            
            self.list_of_fact.append(fact)

    


