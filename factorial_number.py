from itertools import product


def factorial_number(number):
    product=1
    if number == 0:
        print("please enter the value greater then 0.")
    else:
        for num in range(1,number+1):
            product=product*num
    print(product)

factorial_number(5)
def fectorial_recursion(number):
    if number == 0 or number==1:
        return 1
    else:
        return number*fectorial_recursion(number-1)

print(fectorial_recursion(5))
