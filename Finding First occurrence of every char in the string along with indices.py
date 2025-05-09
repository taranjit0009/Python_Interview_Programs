def finding_first_occurrence_of_every_char_in_the_string_along_with_indices():
    string_1 = str(input("Enter you string = "))
    #sorted_string= sorted(string_1)
    print(string_1)
    index=0
    seen_set=set()
    for x in range(len(string_1)):
        #count = 0
        if string_1[x] not in seen_set:
            for y in range(len(string_1)):
                if string_1[x]==string_1[y]:
                    print(f"The first occurrence of {string_1[x]}  at the index : {string_1.index(string_1[x])} ")
                    break
        seen_set.add(string_1[x])
finding_first_occurrence_of_every_char_in_the_string_along_with_indices()
