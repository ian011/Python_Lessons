def main():
    try:
        hours = input("Enter Hours:")
        hours_1=float(hours)
    except:
        print("Please enter an integer value")
    try:
        rate = input("Enter Rate:")
        rate_1=float(rate)
    except:
        print("Please enter an integer value")

    if (hours_1 > 40):
        new_hours= hours_1-40
        pay = 40 * rate_1 + (new_hours*1.5*rate_1)
        print("Your pay is: {}".format(pay))
    else:
      pay1 = hours_1 * rate_1
      print("Your pay is: {}".format(pay1))



    #print("pay",float(hours_1)*float(rate_1))



    #degree=input("Enter temperature in degree celsius:")
    #temp_degree=float(degree)
    #temp_farenheight=(temp_degree*9/5)+32
    #print("in degree celsius:{}".format(temp_farenheight))


    #inp = input('Enter Fahrenheit Temperature:')
    #try:
       # fahr = float(inp)
      #  cel = (fahr - 32.0) * 5.0 / 9.0
     #   print(cel)
    #except:
        #print('Please enter a number')


if __name__ == '__main__':main()
