"""
A prime number is the natural number greater than 1 which has only two factors i.e. 1 and itself.
like 9 is having more than two factors so it's not prime number.
"""
import math


def find_prime_number(number=5):
    count = 0
    if number > 0:
        for n in range(1,number+1):
            if number%n==0:
                count +=1
        if count == 2:
            print(f"{number} is prime number.")
        else:
            print(f"{number} is not prime number.")
    else:
        print("Please enter valid number.")

#find_prime_number(4000000000000)

def find_prime_number_with_short_algo(number):
    if number > 0:
        for n in range(2,int(math.sqrt(number)+1)):
            if number%n==0:
                print(f"{number} is not prime number.")
                break
        else:
            print(f"{number} is prime number.")
find_prime_number_with_short_algo(41)
