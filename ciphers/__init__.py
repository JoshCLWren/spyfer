"""Ciphers in order complexity via http://practicalcryptography.com/ciphers/"""
from dataclasses import dataclass

import ciphers


@dataclass
class Cipher:
    """Base class for ciphers."""

    letters = "abcdefghijklmnopqrstuvwxyz"
    complexity = 0
