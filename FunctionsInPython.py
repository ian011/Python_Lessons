def sum (n1,n2):
    ans=n1+n2
    return ans
def display():
    print("hello man")

def main():
    stra=input("input value to be summed:")
    inta=int (stra)
    strb=input("input a value")
    intb= int (strb)
    z=sum(inta,intb)
    print(z)
    display()

if __name__ == '__main__':main()