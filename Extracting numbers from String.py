def extracting_numbers_from_string():
    str_1 = "hello 23 44 and 22 445 world."
    num_list =[]
    my_list = str_1.split()
    print(my_list)
    for x in my_list:
        if x.isdigit():
            num_list.append(x)
    print(num_list)
extracting_numbers_from_string()