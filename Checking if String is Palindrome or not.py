def checking_if_string_is_palindrome_or_not(value=""):
    reverse= value[::-1]
    if reverse == value:
        print(f'{reverse} is palindrom.')
    else:
        print(value)
        print(f'{reverse} is not palindrom.')

checking_if_string_is_palindrome_or_not("PDsP")