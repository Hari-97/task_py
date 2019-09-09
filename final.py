from factorialofnum import *

class Result(Factorials):
    def display(self):
        Range={}
        j=1
        for i in range(self.start,self.stop):
            Range["Element {}".format(j)]=i
            j+=1
        print("Range = {}".format(Range))

        Sum_of_dig={}
        k=0
        for i in range(self.start,self.stop):
            Sum_of_dig[i]=self.list_of_sum[k]
            k+=1
        print("\nSum of digits = {}".format(Sum_of_dig))

        prime_dict={}
        for i in self.list_of_sum:
            if i in self.prime1:
                prime_dict[i]="Prime"
            else:
                prime_dict[i]="Non-Prime"
        print("\nPrime or Not = {}".format(prime_dict))

        facto={}
        m=0
        for i in self.prime1:
            facto[i]=self.list_of_fact[m]
            m+=1
        print("\nFactorial = {}".format(facto))


if __name__=="__main__":
    
    start=int(input("Enter the start range value : "))
    stop=int(input("Enter the stop value : "))

    obj3=Result(start,stop)
    obj3.addition()
    obj3.findingprimenum()
    obj3.findingfact()
    obj3.display()

        
            

        

        
        
