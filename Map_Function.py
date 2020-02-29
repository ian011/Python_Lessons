def main():
    #without using map function
    ListItems=[3,5,6,7,8,9,10]
    print(ListItems)
    items=[]
    for i in ListItems:
        items.append(i*2)
    print(items)

    #using map function for simplification of code
    ListItems2=list(map(lambda x:x*2,ListItems))
    print(ListItems2)

    ListItems3=list(map(lambda x:x+3,ListItems))
    print(ListItems3)

if __name__ == '__main__':main()
