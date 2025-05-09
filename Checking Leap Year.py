def checking_leap_year():
    year = 1600
    if ((year % 4 == 0 and year % 100!=0) or (year % 400 ==0)):
            print('leap year')
    else:
        print("not leap year")

checking_leap_year()