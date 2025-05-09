def counting_occurrences_of_element_in_list():
    my_list = [2,3,4,5,6,4,3,2,3,4,5,6,5,33,3,4,3,2,2,3,3,4,4,2,2,2,3,3,3,3,3]
    my_list.sort()
    print(my_list)
    value_seen = set()
    for i in range(len(my_list)):
        if my_list[i] not in value_seen:
            count=0
            for j in range(len(my_list)):
                if my_list[i]==my_list[j]:
                    count+=1
            print(f"{my_list[i]} has occured  {count} times.")
            value_seen.add(my_list[i])
counting_occurrences_of_element_in_list()

def counting_occurrences_of_element_in_list_by_count_method():
    my_list = [2, 3, 4, 5, 6, 4, 3, 2, 3, 4, 5, 6, 5, 33, 3, 4, 3, 2, 2, 3, 3, 4, 4, 2, 2, 2, 3, 3, 3, 3, 3]
    x=2
    print("{} has occured times {}.".format(x,my_list.count(x)))
counting_occurrences_of_element_in_list_by_count_method()

from collections import Counter
def counting_occurrences_of_element_in_list_by_dict():
    my_list = [2, 3, 4, 5, 6, 4, 3, 2, 3, 4, 5, 6, 5, 33, 3, 4, 3, 2, 2, 3, 3, 4, 4, 2, 2, 2, 3, 3, 3, 3, 3]
    my_list.sort()
    my_dic = Counter(my_list)
    x=2
    print("{} has occupied {} times.".format(x,my_dic[x]))


counting_occurrences_of_element_in_list_by_dict()


