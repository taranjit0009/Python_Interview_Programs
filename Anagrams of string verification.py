"""
what is anagram of string?
An anagram of a string is a rearrangement(after sorting we will compare the both strings)
of its letters to form a new word or phrase using all the original letters exactly once.
for example, an anagram of 'listen' is 'silent'.
"""

def  anagrams_of_string_verification():
    my_string = "listen"
    my_string2 = "silent"
    #converting both strings into lowercase
    str = my_string.lower()
    str2=my_string2.lower()
    print(sorted(str))
    print(sorted(str2))
    if sorted(str) == sorted(str2):
        print(f'strings {str} are anagram of {str2} each other')
    else:
        print('strings are not anagram of each other')
anagrams_of_string_verification()