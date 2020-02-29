def main():
    #without using a filter
    listitems=[1,2,3,4,5,6,7,8,9]
    items=[]
    for item in listitems:
        if (item%2==0):
            items.append(item)
    print(items)

    #when using a filter
    listitems2=list(filter(lambda x:x%2==0,listitems))
    print(listitems2)




if __name__ == '__main__':main()
