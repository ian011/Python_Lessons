class Car:
    def __init__(self,type,model,year,originalprice,owner):
        self._type=type
        self._Model = model
        self._Year = year
        self._originalprice = originalprice
        self._Owner = owner

    #creates variable named type and assigns value "type" to it
    def getType(self):
        return self._Type
    def getModel(self):
        return self._model
    def getYear(self):
        self._Year=year
    def getoriginalprice(self):
        return self._originalprice
    def getowner(self):
        return self._owner

    def setprice(self,price):
        self._Price = price
    def getprice(self):
        return self._originalprice - (self._Year*1000)

def main():
    mycar= Car("SUV","AUDI R8",10,500000,"IVANKA")

    currentprice = mycar.getprice()
    print("New price is {}".format(currentprice))



if __name__ == '__main__': main()

