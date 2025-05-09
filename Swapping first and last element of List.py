def swapping_first_and_last_element_of_list():
    my_list= [2,3,4,5,6,7,8,9,0]
    first_var = my_list[0]
    my_list[0]=my_list[-1]
    my_list[-1]=first_var
    print(my_list)

    #by swaping
    my_list2 = [9, 3, 4, 5, 6, 7, 8, 9, 10]
    my_list2[0],my_list2[-1]=my_list2[-1],my_list2[0]

    print(my_list2)

swapping_first_and_last_element_of_list()

def swapinng_any_element():
    my_list = [9, 3, 4, 5, 6, 7, 8, 9, 10]
    index_ele_1 = 3
    index_ele_2=5
    my_list[index_ele_1],my_list[index_ele_2]=my_list[index_ele_2],my_list[index_ele_1]
    print(my_list)

swapinng_any_element()