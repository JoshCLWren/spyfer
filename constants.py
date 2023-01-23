BACON_DICT = {
    "aaaaa": "A",
    "aaaab": "B",
    "aaaba": "C",
    "aaabb": "D",
    "aabaa": "E",
    "aabab": "F",
    "aabba": "G",
    "aabbb": "H",
    "abaaa": "I",
    "abaab": "J",
    "ababa": "K",
    "ababb": "L",
    "abbaa": "M",
    "abbab": "N",
    "abbba": "O",
    "abbbb": "P",
    "baaaa": "Q",
    "baaab": "R",
    "baaba": "S",
    "baabb": "T",
    "babaa": "U",
    "babab": "V",
    "babba": "W",
    "babbb": "X",
    "bbaaa": "Y",
    "bbaab": "Z",
}

REVERSE_BACON_DICT = {v: k for k, v in BACON_DICT.items()}

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
END = "\033[0m"


def all_words():
    words_list = []
    with open("english.txt", "r") as f:
        words_list.extend(line.strip() for line in f)
    return words_list


# create a list of all strings in english.txt
WORDS = all_words()

COUNTRY_DESCRIPTIONS = ["beautiful", "breezy", "balmy", "sticky"]
