"""
A spy game written in Python.
You're an international spy. You have been given a series of messages to encode without the enemy knowing.
The computer will try and brute force the messages and send the enemy your messages.
Pick a cipher and encode the message. The computer will try and decode it.
"""

import random
import string
import sys
import time
from dataclasses import dataclass
from typing import List, Tuple

import pandas as pd
import pycountry
import requests
from faker import Faker

import ciphers
import ciphers.atbash as atbash
import ciphers.baconian as baconian
import ciphers.caesar as caesar
import constants

fake = Faker()


def simple_decrypt(i, ciphertext):
    """Brute force decryption of ciphertext using Atbash cipher"""
    plaintext = "".join(
        chr((ord(char) - i - ord("a")) % 26 + ord("a")) if char.isalpha() else char
        for char in ciphertext
    )
    delay_print(f"Guess #{str(i + 1)} is it {plaintext}?")
    return plaintext


def decrypt_bacon(ciphertext):
    """Brute force decryption of ciphertext using Baconian cipher"""

    plaintext = ""
    for i in range(0, len(ciphertext), 5):
        letter = ciphertext[i : i + 5]
        if letter in constants.BACON_DICT:
            plaintext += constants.BACON_DICT[letter]
    delay_print("Plaintext:", plaintext)
    return plaintext


class Player:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.lives = 3

    def lose_life(self):
        self.lives -= 1
        if self.lives == 0:
            delay_print("You lose!")
            sys.exit()
        else:
            delay_print(f"You have {self.lives} lives left.")


def delay_print(*args, delay=0.01, color=None):
    """
    Print to stdout one character at a time like a typewriter with a delay between each character
    in the color specified.
    """
    if color:
        print(color, end="")

    for arg in args:
        for char in arg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
    print()


def main():
    """The main function."""
    kanye_quotes = pd.read_csv("kanye_quotes.csv")
    insults = pd.read_csv("insults.csv")
    player = Player()
    location = pycountry.countries.get(alpha_2="US").name
    delay_print(f"Welcome to the {location}!", delay=0.05, color=constants.GREEN)
    delay_print(f"You are a {get_insult(insults)}spy for the CIA.")
    delay_print(
        "You have been tasked with encoding and sending a series of messages by rogue Sleeper Cell agent Kanye West.",
        color=constants.RED,
    )
    delay_print("You have three lives.", delay=0.10, color=constants.GREEN)
    menu_options(
        f"This is not a {get_insult(insults)}communication channel. Do not use it for anything important.",
        "You are an international spy. You have been given a series of messages to encode and decode.",
        "The computer will try and brute force the messages and send the enemy your messages.",
        "Pick a cipher and encode the message. The computer will try and decode it.",
    )
    instructions(
        "The lower the score, the better.",
        "You have 10 attempts to get the correct answer.",
        "Decode your first message.",
    )
    while player.lives > 0:
        delay_print(f"Level: {player.level}", delay=0.05, color=constants.BLUE)
        delay_print(f"Lives: {player.lives}", delay=0.05, color=constants.BLUE)
        delay_print(f"Score: {player.score}", delay=0.05, color=constants.BLUE)
        # Get a random quote from the Kanye West pandas dataframe
        message = kanye_quotes.sample().iloc[0]["quote"]
        delay_print(
            f"Your {get_insult(insults)}message from {get_insult(insults)}Mr. West is: {message}",
            delay=0.05,
            color=constants.RED,
        )
        cipher_map = {
            "1": caesar.Caesar(key=13).encode,
            "2": ciphers.atbash.encode,
            "3": ciphers.baconian.encode,
        }
        menu_options(
            f"Which {get_insult(insults)}cipher are you using?",
            "1. Caesar",
            "2. Atbash",
            "3. Baconian",
        )
        cipher = input()

        score = 0

        cipher = cipher_map[cipher](message)
        menu_options(
            "Your encoded message is:",
            cipher,
            "Sending message...",
            "The computer is trying to decode your message!",
        )
        # brute force the message by randomly guessing characters
        attempts = player.level * 2
        for i in range(attempts):
            delay_print(f"Attempt {str(i + 1)}")
            for i in range(random.randint(1, attempts)):
                guess = simple_decrypt(i, cipher)
                if guess == cipher:
                    delay_print("The enemy computer guessed correctly!")
                    player.lose_life()
                else:
                    delay_print("The computer guessed incorrectly.")
                    player.score += 1
                guess = decrypt_bacon(cipher)
                if guess == cipher:
                    delay_print("The enemy computer guessed correctly!")
                    player.lose_life()
                else:
                    delay_print("The computer guessed incorrectly.")
                    player.score += 1

        delay_print(f"Your score is {score}")
        player.level += 1
        delay_print(f"You have completed level {str(player.level - 1)}")
        delay_print(f"You have {str(player.lives)} lives left.")
        delay_print(f"You have {str(player.score)} points.")
        new_random_location = list(pycountry.countries)[random.randint(0, 250)].name
        delay_print(
            f"You've moved to {new_random_location}! To further mask your location, you've changed your name to {fake.name()}."
        )
        delay_print("You have been given a new message to decode.")


def get_insult(insults):
    return insults.sample().iloc[0]["insult"]


def instructions(arg0, arg1, arg2):
    delay_print(arg0, delay=0, color=constants.GREEN)
    delay_print(arg1, delay=0, color=constants.GREEN)

    delay_print(arg2, delay=0, color=constants.GREEN)


def menu_options(arg0, arg1, arg2, arg3):
    instructions(arg0, arg1, arg2)
    delay_print(arg3, delay=0, color=constants.GREEN)


if __name__ == "__main__":
    main()
