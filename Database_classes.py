import sqlite3
class DBConnect:
    def __init__(self):
        self._db = sqlite3.connect("information db")#connects to information database
        #defining a function that creates tables in sqlite
        self._db.row_factory = sqlite3.Row
        self._db.execute("create table if not exists Admin(ID integer primary key autoincrement, Name text, Age int)")
        self._db.commit()

        #defining a function that adds data on the table created
    def adding (self,Name,Age):
        self._db.execute("insert into Admin(Name,Age) values(?,?)",(Name, Age))
        print("data added")
        self._db.commit()
    #defining a function that displays admin list in the program
    def ShowList (self):
        cursor=self._db.execute('select * from Admin')
        for row in cursor:
            print("ID : {}, Name : {}, \n Age : {}".format(row["ID"],row["Name"],row ["Age"]))
    #defining a function to delete the records
    def DeleteRecord (self,ID):
        self._db.row_factory= sqlite3.Row
        self._db.execute("delete from admin where ID ={}".format(ID))
        self._db.commit()
    #defining function that updates age of people
    def UpdateRecord(self,ID,Age):
        self._db.execute("update Admin set Age=? where ID=?", (Age, ID))
        print("data updated")
        self._db.commit()