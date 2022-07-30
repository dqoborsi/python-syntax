def print_upper_words(list, must_start_with):
    """Prints each word in a list as all uppercase"""
    for word in list:
        if word[0].lower() in must_start_with:
            print(word.upper())

print(print_upper_words(['aaa','bbb','ccc','ddd','eee', 'hhh', 'yyy'], {'h', 'y'}))