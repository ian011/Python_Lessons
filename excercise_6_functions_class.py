def computepay(hours_1,rate_1):

    if (hours_1 > 40):
        new_hours= hours_1-40
        pay_with_overtime = 40 * rate_1 + (new_hours*1.5*rate_1)
        print("Your pay is: {}".format(pay_with_overtime))
    else:
      pay1 = hours_1 * rate_1
      print("Your pay is: {}".format(pay1))

def main():
    try:
        hours = input("Enter Hours:")
        hours_1 = float(hours)
    except:
        print("Please enter an integer value")
    try:
        rate = input("Enter Rate:")
        rate_1 = float(rate)
    except:
        print("Please enter an integer value")

    computepay(hours_1 , rate_1)


if __name__ == '__main__': main()
