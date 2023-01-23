"""
Vigenere Cipher
Description:
    The Vigenere cipher is a polyalphabetic substitution cipher. It is a
    generalization of the Caesar cipher. It is a type of autokey cipher.
    It uses a series of Caesar ciphers based on the letters of a keyword.
    It is a form of polyalphabetic substitution.
Algorithm:
    Ei = (Pi + Ki) mod 26
    Di = (Ei - Ki + 26) mod 26
Complexity:
    O(n)
Example:
    "Encode this" with key "key" -> "Lgqjxg yqj"
"""

import string

import constants
from ciphers import Cipher


class Vigenere:
    def __init__(self, key):
        self.key = key

    def encode(self, plaintext):
        key_len = len(self.key)
        key_as_int = [ord(i) for i in self.key]
        plaintext_int = [ord(i) for i in plaintext]
        return "".join(
            chr((plaintext_int[i] + key_as_int[i % key_len]) % 26 + ord("A"))
            for i in range(len(plaintext_int))
        )

    def decode(self, ciphertext):
        key_len = len(self.key)
        key_as_int = [ord(i) for i in self.key]
        ciphertext_int = [ord(i) for i in ciphertext]
        return "".join(
            chr((ciphertext_int[i] - key_as_int[i % key_len] + 26) % 26 + ord("A"))
            for i in range(len(ciphertext_int))
        )
