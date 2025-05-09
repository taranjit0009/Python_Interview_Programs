def copy_or_clone_the_list():
    my_list = [10,3,4,2,1,2,3,4,43,2,2,3,3]
    #useing copy() method
    copy_list=my_list.copy()
    print(copy_list)
    #assign list to another list
    cop_list = my_list
    print(cop_list)
    #extend method
    copy_list_1 = []
    copy_list_1.extend(my_list)
    print(copy_list_1)
    #slicing approach
    cop_list_3 = my_list[:]
    print(cop_list_3)
    #by list  method
    cop_list_4 = list(my_list)
    print(cop_list_4)
    #by list comprehension
    cop_list_5= [x for x in my_list]
    print(cop_list_5)

copy_or_clone_the_list()