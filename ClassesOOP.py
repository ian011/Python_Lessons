class user:
    def __init__(self,UserName,age):
       # print("great object")
    #def setUserName (self,UserName):
        self._UserName=UserName
        self._Age=age
    def getUserName (self):
        return self._UserName
    def getUserAge(self):
        return self._Age


def main():
    u1=user("Ian Bosco",23)
    #u1.setUserName("Ian Bosco")
    print( u1.getUserName())
    print(u1.getUserAge())


    u2=user("Michael Bolton",21)
    #u2.setUserName("Michael Bolton")
    print(u2.getUserName())
    print(u2.getUserAge())


if __name__ == '__main__':main()
