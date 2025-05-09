import math
def multiplying_all_numbers_from_list():
    my_list = [2, 3, 4, 5, 6, 7, 8, 9]
    print(math.prod(my_list))
    sum1 = 1
    for x in range(len(my_list)):
        sum1 *= my_list[x]
    print(sum1)

multiplying_all_numbers_from_list()