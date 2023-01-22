"""
Caesar Cipher
"""

from dataclasses import dataclass
from typing import List, Tuple

from ciphers import Cipher


@dataclass
class Caesar(Cipher):
    """
    The Caesar cipher is a substitution cipher where each letter in the alphabet is shifted a certain
    number of places down the alphabet. For example, with a shift of 3, A would be replaced with D,
    B would become E, and so on. The method is named after Julius Caesar, who apparently used it to
    communicate with his generals.

    """

    complexity = 2
    key: int

    def encode(self, message):
        """Encrypt message."""
        message = message.lower()
        return "".join(
            self.letters[(self.letters.index(letter) + self.key) % 26]
            if letter in self.letters
            else letter
            for letter in message
        )

    def decode(self, ciphertext):
        """Decrypt ciphertext."""
        ciphertext = ciphertext.lower()
        return "".join(
            self.letters[(self.letters.index(letter) - self.key) % 26]
            if letter in self.letters
            else letter
            for letter in ciphertext
        )
