


def isLeapYear(year):

        if(year%4==0 and year%100!= 0 or year%400==0):
            print("The year is a leap year!")
            return True
        else:
            print("The year isn t a leap year! ")
            return False



resultIs = isLeapYear(2000)
print(resultIs)


