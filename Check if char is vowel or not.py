def check_if_char_is_vowel_or_not():
    vowel = ['a','e','i','o','u']
    value = str(input("Enter the English alphabet = "))
    if value.lower() in vowel:
        print(f'Yes {value} is vowel.')
    else:
        print(f'Yes {value} is not vowel.')

check_if_char_is_vowel_or_not()