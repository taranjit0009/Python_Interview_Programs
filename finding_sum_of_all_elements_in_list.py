def finding_sum_of_all_elements_in_list():
    my_list = [2,3,4,5,6,7,8,9]
    print(sum(my_list))
    sum1=0
    for x in range(len(my_list)):
        sum1 += my_list[x]
    print(sum1)
finding_sum_of_all_elements_in_list()