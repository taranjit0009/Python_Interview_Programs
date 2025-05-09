"""
Checking if String contains special character => We use regular expression
"""
import re
def checking_if_string_contains_special_character():
    sting_1 = "hghagkjh^&*&"
    sting_2="HelloWorld"
    regex = re.compile('[!@#$%^&*()_{}"?/.,<>]')
    if regex.search(sting_1) is None:
        print("String does not contain special char")
    else:
        print("String does contain special char")

checking_if_string_contains_special_character()