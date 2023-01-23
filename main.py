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

import art
import pandas as pd
import pycountry
import requests
from faker import Faker

import ciphers
import ciphers.atbash as atbash
import ciphers.baconian as baconian
import ciphers.caesar as caesar
import ciphers.vigenere as vigenere
import constants

fake = Faker()

import itertools


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


class BruteForceGuesser:
    def __init__(self, string_to_guess, charset, attempts):
        self.string_to_guess = string_to_guess
        self.charset = charset
        self.attempts = attempts

    def guess(self):
        """Guess the string using brute force but with a limited number of attempts"""
        for attempt in range(self.attempts * 2):
            guess = "".join(
                random.choice(self.charset) for _ in range(len(self.string_to_guess))
            )
            delay_print(f"Attempt {attempt}: {guess}")
            if guess == self.string_to_guess:
                delay_print(f"Success! The password was {guess}")
                return True


# Usage example


def simple_decrypt(i, ciphertext):
    """Brute force decryption of ciphertext using Atbash/Caesar cipher"""
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

    def level_up(self):
        self.level += 1
        delay_print(f"You are now level {self.level}.")


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
    delay_print(art.text2art("Spyfer, a 'game'.", font="cybermedium"))
    art.tprint(f"Welcome to the {location}!", font="cybermedium")
    delay_print(f"You are a {get_insult(insults)}spy for the CIA.")
    delay_print(
        "You have been tasked with encoding and sending a series of messages by rogue Sleeper Cell agent Kanye West.",
        color=constants.RED,
    )
    delay_print("You have three lives.", delay=0.10, color=constants.GREEN)
    menu_options(
        f"This is not a {get_insult(insults)}communication channel. Do not use it for anything important.",
        "You are an international spy. You have been given a series of messages to encode and decode.",
        "The Evil Vigenere AI has gained sentience and is hot on our trails.",
        "Pick a cipher and encode the message. The computer will try and decode it.",
    )
    instructions(
        "The lower the score, the better.",
        "You have 10 attempts to get the correct answer.",
        "Decode your first message.",
    )
    while player.lives > 0:
        art.tprint(f"Level: {player.level}")
        art.tprint(f"Lives: {player.lives}")
        art.tprint(f"Score: {player.score}")
        # Get a random quote from the Kanye West pandas dataframe
        message = kanye_quotes.sample().iloc[0]["quote"]
        delay_print(
            f"Your {get_insult(insults)}message from {get_insult(insults)}Mr. West is:",
            delay=0.05,
            color=constants.RED,
        )
        delay_print(message, delay=0.05, color=constants.BLUE)
        score = 0
        delay_print(
            f"Choose a {player.level + 3} character password using only the letters from the your current location."
        )
        delay_print("Oh, and it has to also be a real word.")
        password = input()
        if password == "quit":
            sys.exit()

        # Check if the password is correct
        if password.lower() not in constants.WORDS:
            delay_print("That's not a real word, at least by my standards.")
            delay_print(
                f"An example of a real word is {random.choice(constants.WORDS)}"
            )
            delay_print("You're going to get us killed!.", color=constants.RED)
            delay_print("I'm not made, I'm dissapointed.", color=constants.RED)

            player.lose_life()
            continue
        if password.lower() not in location.lower():
            delay_print("You're going to get us killed!.", color=constants.RED)
            delay_print("You lose a life.")
            delay_print("The enemy has intercepted your message.")
            delay_print(
                "They're one step closer to knowing not just our location, but our identity."
            )
            player.lose_life()
            continue
        if len(password) != player.level + 3:
            delay_print(
                "You're going to get us killed by not following instructions!.",
                color=constants.RED,
            )
            delay_print(f"Your password must be {player.level + 3} characters long.")
            delay_print(
                f"The password you entered was {len(password)} characters long."
            )
            delay_print(f"Do you hate {location}?")
            delay_print("You lose a life.")
            delay_print("The enemy has intercepted your message.")
            delay_print(
                "They're one step closer to knowing not just our location, but our identity."
            )
            player.lose_life()
            continue
        cipher = vigenere.Vigenere(key=password).encode(message)
        menu_options(
            "Your encoded message is:",
            cipher,
            "Sending message...",
            "The Vigenere computer is trying to decode your message!",
        )
        # brute force the message by randomly guessing characters
        attempts = player.level * fibonacci(player.level)
        guesser = BruteForceGuesser(password, "abcdefghijklmnopqrstuvwxyz", attempts)
        if guesser.guess():
            delay_print("The Vigenere computer guessed your message!")
            delay_print("You lost a life.")
            player.lives -= 1
        else:
            delay_print("The computer failed to guess your message.")
            delay_print("You gained a level.")
            player.level_up()
            player.score += 1 * player.level
        # for i in range(attempts):
        #     delay_print(f"Attempt {str(i + 1)}")
        #     for i in range(random.randint(1, attempts)):
        #         guess = simple_decrypt(i, cipher)
        #         if guess == cipher:
        #             delay_print("The enemy computer guessed correctly!")
        #             player.lose_life()
        #         else:
        #             delay_print("The computer guessed incorrectly.")
        #             player.score += 1
        #         guess = decrypt_bacon(cipher)
        #         if guess == cipher:
        #             delay_print("The enemy computer guessed correctly!")
        #             player.lose_life()
        #         else:
        #             delay_print("The computer guessed incorrectly.")
        #             player.score += 1

        delay_print(f"Your score is {score}")
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
