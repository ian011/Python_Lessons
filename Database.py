from Database_classes import DBConnect
def main():
    DBconnection=DBConnect()  #calling the createdatabase function
    while 1:
        index0p=int(input(":select your option\n1 for adding\n2 to display admin list"
                          "\n3 to delete a name\n4 to update age of the person\n0 to exit\nenter index operation:"))
        print("\n===============================================\n")

        if (index0p==0):
            break;
        if (index0p==1):
            Name = input("ENTER THE NAME:")
            Age = int(input("Enter the persons AGE:"))
            DBconnection.adding(Name,Age)
        elif(index0p==2):
            DBconnection.ShowList()
        elif(index0p==3):
            ID=int(input("enter the ID to be deleted:"))
            DBconnection.DeleteRecord(ID)
        elif(index0p==4):
            ID = int(input("enter the id of person whose age is to be updated:"))
            Age = int(input("Enter the persons new age:"))
            DBconnection.UpdateRecord(ID, Age)




if __name__ == '__main__' :  main()

