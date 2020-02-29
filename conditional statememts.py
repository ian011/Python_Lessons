import datetime
DOB = "2000"    #input("enter your year of birth :")
CurrentYear= datetime.datetime.now().year
age=int(CurrentYear)-int(DOB)
if (age>=16):
    print("your age is {} and you can drive".format(age))
if (age<16):
    print("your age is {} and you cannot drive yet".format(age))
print("program complete")

number=20       #input("Enter a value:")
if(int(number)>0):
    print("the number is positive")
elif(int(number)==0):
    print("number is zero")
else:
    print("the number is bloody negative")
print("program complete")

strmark=input("enter your average mark:")
mark=int(strmark)
if(mark>=90):
    print("your grade is A")
elif(mark>=80 and mark<90):
    print("Your grade is B")
elif(mark>=70 and mark <80):
    print("your grade is C")
else:
    print("you failed the test")