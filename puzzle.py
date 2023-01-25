def possible_words(location, length_of_word):
    """
    Find the all the words that both only use characters
    in the location and are the same length as the string to guess
    That are in english.txt
    """
    with open("english.txt") as f:
        english_words = f.read().splitlines()

    return [
        word
        for word in english_words
        if all(char in location for char in word) and len(word) == length_of_word
    ]
