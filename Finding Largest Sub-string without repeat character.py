from operator import index


def finding_largest_sub_string_without_repeat_character():
    string="Welcome Back Taranjit Singh Bains Singh. karanjit"
    longest_word=''
    li = string.split(' ')
    li.sort()
    print(li)
    highest_length_string = {}
    length=0
    for x in range(len(li)):
        if len(li[x])>=length:
            length=len(li[x])
            longest_word=li[x]

    highest_length_string.update({longest_word:length})
    print(highest_length_string)
finding_largest_sub_string_without_repeat_character()

#print(f"{longest_word} = {length}")
