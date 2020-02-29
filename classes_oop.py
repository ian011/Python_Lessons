class operations:
    def sum(self,n1,n2):
        return n1+n2
    def subtraction(self,n1,n2):
        return n1-n2
class multioperations(operations):
    def division(self,n1,n2):
        return n1/n2
    def sum(self,n1,n2):
        return (n1+n2)*2  #this is an override
        #return super().sum(n1,n2) #calling a specific method from the parent class
