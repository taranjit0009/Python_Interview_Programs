def removing_special_chars_and_numbers_from_string():
    string_1 = '%^$@&^hgkghhghsk96879 dsfwf6*(&@*&'
    result = ""
    for x in string_1:
        if x.isalpha():
            result+=x

    print(result)


removing_special_chars_and_numbers_from_string()