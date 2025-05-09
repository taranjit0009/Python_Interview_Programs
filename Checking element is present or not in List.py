def checking_element_is_present_or_not_in_list():
    my_list=[2,3,4,5,6,7,8,9]
    ele=4
    flag=0
    for i in range(len(my_list)):
        if my_list[i] == ele:
            print(f'Element {ele} is present in the list.')
            flag+=1
    if flag==0:
        print(f'Element {ele} not present in the list.')

checking_element_is_present_or_not_in_list()