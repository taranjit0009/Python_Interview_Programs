def finding_first_character_of_each_word_in_sentence():
    string_1 = str(input("Enter the sentence = "))
    li= string_1.split(" ")
    output_result = ""
    for x in range(len(li)):
        output_result+=li[x][0]

    print(type(output_result))
    print(output_result)
finding_first_character_of_each_word_in_sentence()