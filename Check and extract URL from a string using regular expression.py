import re
def check_and_extract_URL_from_a_string_using_regular_expression():
    #r"..." raw string syntax for the regex is recommended
    url_pattern = r"https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    string_1 = "Hello World https://www.google.com"
    string_2="Hello World http://www.google.com ,Hello World https://www.google.com"
    url_1=re.findall(url_pattern,string_1)
    print(url_1)
    url_2  =re.findall(url_pattern,string_2)
    print(url_2)
check_and_extract_URL_from_a_string_using_regular_expression()