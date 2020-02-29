strAge=input("enter your age:")
age=int(strAge)
if (age>18):
    print("you are eligible to enroll in our classes")
    if (age<30):
        print("you are in class A")
    else:
        print("you are in class B")
else:
    print("sorry you are not eligible to enroll for this service")