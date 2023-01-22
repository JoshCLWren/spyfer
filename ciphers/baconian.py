import constants


def decode(ciphertext):
    """Decrypt ciphertext using Baconian cipher"""
    plaintext = ""
    for i in range(0, len(ciphertext), 5):
        letter = ciphertext[i : i + 5]
        for key, value in constants.BACON_DICT.items():
            if letter == value:
                plaintext += key
    return plaintext


def encode(plaintext):
    """Encrypt plaintext using Baconian cipher"""
    plaintext = plaintext.upper()
    return "".join(
        constants.REVERSE_BACON_DICT[char]
        for char in plaintext
        if char in constants.ALPHABET
    )
