i=0
while (i<5):
    j=0
    while(j<3):
        if (i==j):
         print("(i , j) = ({},{})".format(i,j))
        j+=1
    i+=1

#APPLICATION OF BREAK AND CONTINUE
word = "python"
for letter in word:
    #if (letter=="h"):
     #   break;
    if(letter=="t"):
        continue;

    print(letter)

l=[22,32,65,76,78,89,12,34]
for item in l:
    if (item == 89):
        print("number is found")
        break;
print("app is done")