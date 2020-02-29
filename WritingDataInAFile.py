def main():
    #WRITING DATA INTO A FILE
    #out = open("test.txt","w")
    #for i in range (5):
      #data = input("enter string input: ")
     # out.write("\n your name is:{}".format(data))
   # out.close()
    #READING DATA FROM A FILE
    readfile = open("test.txt","r")
    for line in readfile:
        print(line)
    readfile.close



if __name__ == "__main__":main()
