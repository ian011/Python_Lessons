def main():
    from functools import reduce
    listitems=[1,2,3,4,5,6,7,8,9]
    sum=0
    for item in listitems:
        sum=sum+item
    print(sum)
    #using reduce
    sum1=reduce(lambda x,y:x+y,listitems)
    print(sum1)


if __name__ == '__main__':main()
