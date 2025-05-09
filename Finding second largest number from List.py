def finding_second_largest_number_from_list():
    my_list = [2,34,34,3455344,53,23,35,4565,6543,243,2643432,2,3,2,34]
    remove_duplicates=set(my_list)
    my_list = list(remove_duplicates)
    my_list.sort()
    print(my_list)
    print(my_list[-2])

finding_second_largest_number_from_list()