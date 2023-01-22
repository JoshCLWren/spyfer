import constants


def encode(plaintext):
    """Encrypt plaintext using Atbash cipher"""
    return "".join(
        constants.ALPHABET[25 - constants.ALPHABET.index(char)]
        if char in constants.ALPHABET
        else char
        for char in plaintext.lower()
    )


def decode(ciphertext):
    """Decrypt ciphertext using Atbash cipher"""
    return "".join(
        constants.ALPHABET[25 - constants.ALPHABET.index(char)]
        if char in constants.ALPHABET
        else char
        for char in ciphertext.lower()
    )


# # usage example
# atbash = Atbash()
# ciphertext = atbash.encode("hello world")
# delay_print(ciphertext) # svool dliow
# plaintext = atbash.decode(ciphertext)
# delay_print(plaintext) # hello world
