def displaying_frequency_of_each_character_in_string():
    string_1 = "Hello world"
    dic={}
    for x in string_1:
        if x in dic.keys():
            dic[x]=dic[x]+1
        else:
            dic[x]=1
    print(dic)

displaying_frequency_of_each_character_in_string()