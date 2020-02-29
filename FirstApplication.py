import datetime
date_time = datetime.datetime.now()
print(date_time)

#GETTING DATE AND TIME FROM A GIVEN TIMESTAMP
from datetime import date   #IMPORT DATE CLASS ALONE FROM THE DATETIME MODULE
timestamp = date.fromtimestamp(1326244364) #using fromtimestamp method
print("Date = ",timestamp)

#DOB =input("enter your year of birth :")
#CurrentYear=input("enter the current year :")
#age=int(CurrentYear)-int(DOB)
#print("your bloody age is {} and you were born in {}".format(age,DOB))


Year=1997
Age=2019-Year
agemessage="your age is {} and the Year you were born is {}".format(Age,Year)
#print(agemessage)

from django.template.defaultfilters import upper, lower
name ="Tedd Cruz"
strlenght = (len(name))
print(strlenght)
print(upper(name))
print(lower(name))

