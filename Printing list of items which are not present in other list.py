def printing_list_of_items_which_are_not_present_in_other_list():
    li_1= ["apple",'banana','orange']
    li_2 = ["banana","Mango","cheery","orange"]
    set_1 = set(li_1)
    set_2=set(li_2)
    li=list(set_1.difference(set_2))
    print(li)

printing_list_of_items_which_are_not_present_in_other_list()