"""
a series of numbers in which each number (Fibonacci nnumber) is the sum of the
two preceding numbers.The simplest is the series 0,1,1,2,3,5,8,... etc.
0,1,1,2,3,5,8,13
n1=0,n2=1
"""

def find_fibonacci_number(number):
    num1 = 0
    num2=1
    sum=0
    for _ in range(0,number):
        print(num2,end='')
        sum = num1+num2
        num1=num2
        num2=sum
    print()
    print(sum)

find_fibonacci_number(5)