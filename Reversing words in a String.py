def reversing_words_in_a_string(value=""):
    outcome = value.split(' ')
    reverse = outcome[-1::-1]
    result = " ".join(reverse)
    print(result)

reversing_words_in_a_string("Taranjit Singh Bains")