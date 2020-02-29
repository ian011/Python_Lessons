class Car:
    def __init__(self,**kwargs):
        self._Data=kwargs
  #creates variable named type and assigns value "type" to it
    def getowner(self):
        return self._Data["owner"]
    def getType(self):
        return self._Data["type"]
    def getModel(self):
        return self._Data["model"]
    def getYear(self):
         return self._Data["year"]
    def getoriginal(self):
         return self._Data["original"]
    def setprice(self, price):
        self._Price = price

    def getprice(self):
        return self.getoriginal() - (self.getYear() * 1000)




    # ++**********



def main():
    mycar= Car(owner="IVANKA", type="SUV",model="AUDI R8",year=10,originalprice=500000)
    currentprice = mycar.getprice()
    owner=mycar.getowner()
    print("{} New price is {}".format(owner,currentprice))



if __name__ == '__main__': main()

