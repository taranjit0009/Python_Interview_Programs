def finding_most_repeated_character_in_string():
    string_1 = str(input('Enter the string = ')).strip().replace(" ",'')
    #string_1 = "welcome to Indiaaaaa".strip().replace(" ",'')
    sorted_string = sorted(string_1)
    print(sorted_string)
    most_repeated_char = ""
    max_count = 0
    seen_set=set()
    for x in range(0,len(sorted_string)):
        length = 0
        if sorted_string[x] not in seen_set:
            for y in range(0,len(sorted_string)):
                #debugging
                #print(sorted_string[x],sorted_string[y])
                if sorted_string[x]==sorted_string[y]:
                    length+=1
            seen_set.add(sorted_string[x])
            #print(f"{sorted_string[x]}={length}")
            if length>max_count:
                max_count=length
                most_repeated_char=sorted_string[x]
    print(f"The most repeted char is {most_repeated_char} = {max_count}")
finding_most_repeated_character_in_string()