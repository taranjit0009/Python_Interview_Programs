def check_if_any_number_is_common_between_two_lists():
    list_1 = [12]
    list_2=[2,3,4,5,6,7,8,12]
    set_1 = set(list_1)
    set_2 = set(list_2)
    list_3=list(set_1.intersection(set_2))
    print(list_3)
check_if_any_number_is_common_between_two_lists()

def if_number_is_common():
    list_1 = [12]
    list_2 = [2, 3, 4, 5, 6, 7, 8, 12]
    for x in list_1:
        for j in list_2:
            if x==j:
                print(True)
        else:
            print(False)

if_number_is_common()