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

insults = pd.read_csv("insults.csv")


def get_insult(insults):
    return insults.sample().iloc[0]["insult"]


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


class BruteForceGuesser:
    def __init__(self, string_to_guess, charset, attempts, location):
        self.string_to_guess = string_to_guess
        self.charset = charset
        self.attempts = attempts
        self.possibilities = possible_words(location, len(self.string_to_guess))

    def guess(self):
        """
        Make n amounts of random guesses from Possibilities to try and guess the string to guess
        """
        delay_print(
            "It is I, Vigenere, the great cipher. I will try and guess your message."
        )
        delay_print(
            f"First I will guess your weight in pounds, are you {random.randint(250,400)}lbs?"
        )
        delay_print(
            f"Next I will guess your age, are you {random.randint(20,40)} years old?"
        )
        delay_print(
            f"Next I will guess your height in inches, are you {random.randint(60,80)} inches tall?"
        )
        delay_print(f"Is your name {fake.name()}?")
        delay_print(f"Is your address {fake.address()}?")
        delay_print(f"Is your email {fake.email()}?")
        delay_print(f"Is your phone number {fake.phone_number()}?")
        delay_print(f"Is your credit card number {fake.credit_card_number()}?")
        delay_print(f"Is your SSN {fake.ssn()}?")
        delay_print(f"Is your username {fake.user_name()}?")
        delay_print(f"Is your password {fake.password()}?")
        delay_print(f"Is your job {fake.job()}?")
        delay_print(f"Is your company {fake.company()}?")
        delay_print(f"Is your country {fake.country()}?")
        delay_print(f"Is your city {fake.city()}?")
        delay_print(f"Is your state {fake.state()}?")
        delay_print(f"Is your zipcode {fake.zipcode()}?")
        delay_print(f"Is your license plate {fake.license_plate()}?")
        delay_print(f"Agent, there are only {len(self.possibilities)} possibilities.")
        delay_print("I will try and guess the message.")

        for _ in range(self.attempts):
            guess = random.choice(self.possibilities)
            delay_print(f"I'm guessing {guess}")
            if guess == self.string_to_guess:
                delay_print("I guessed it!")
                return True
        delay_print("I couldn't guess it.")
        return False


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
    def __init__(self, name, location):
        self.score = 0
        self.level = 1
        self.respect = 3
        self.name = name
        self.adjective = get_insult(insults)
        self.location = location

    def lose_respect(self):
        self.respect -= 1
        if self.respect == 0:
            delay_print("I've lost all confidence in you!")
            sys.exit()
        else:
            delay_print(f"You have {self.respect} respect left with me.")

    def change_adjective(self):
        self.adjective = get_insult(insults)
        delay_print(f"You are now {self.adjective}.")

    def level_up(self):
        self.level += 1
        self.change_adjective()
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

    location = pycountry.countries.get(alpha_2="US").name
    delay_print(art.text2art("Spyfer, a 'game'.", font="cybermedium"))
    art.tprint(
        f"Welcome to the {random.choice(constants.COUNTRY_DESCRIPTIONS)} {location}!",
    )
    fake_name = fake.name()
    delay_print(
        f"What's your name? press enter to go with {fake_name}. You look like a {fake_name}.",
        color=constants.GREEN,
    )
    name = input() or fake_name
    if name.lower() in "kanye west":
        delay_print(
            "Nice Try KANYE! You're the bad guy in this game go play something else!"
        )
        sys.exit()

    player = Player(name, location)
    delay_print(f"Welcome to the mission, {player.name}!")
    delay_print(f"According to our records, you are a {player.adjective}spy.")
    delay_print(f"I respect you, {player.name}.")
    delay_print(f"You currently have {player.respect} respect with me.")
    delay_print(
        "You have been tasked with encoding and sending a series of messages by everybody's failed government "
        "experiment gone rogue: Kanye West.",
        color=constants.RED,
    )
    delay_print("Kanye West has -1 respect with me.", color=constants.RED)
    delay_print("You have three lives to live.", delay=0.10, color=constants.GREEN)
    menu_options(
        f"This is not a {get_insult(insults)}communication channel. Do not use it for anything important.",
        "The Evil Vigenere AI has gained sentience and is hot on our trails.",
        "Pick a cipher and encode the message. The AI will try and decode it.",
    )
    instructions(
        "The lower the score, the better.",
        "You have 10 attempts to get the correct answer.",
        "Decode your first message.",
    )
    while player.respect > 0:
        message, password, points, score = begin_round(kanye_quotes, player)
        if not password:
            # create a list of 3 words of the correct lenght but only one is in the location
            try:
                real_hint = random.choices(
                    possible_words(player.location, player.level + 3)
                )
                random_location = list(pycountry.countries)[random.randint(0, 250)].name
                fake_hints = random.choices(
                    possible_words(random_location, player.level + 3), k=2
                )
                hints = real_hint + fake_hints
                delay_print("Here are your hints:")
                for hint in hints:
                    delay_print(hint)
                points -= 1
                delay_print(
                    "Type the password you'd like to use knowing that only one of the hints is correct."
                )
                delay_print(
                    "Don't enter some clever word you've just found that matches the criteria, it's too late for that."
                )
                delay_print("Which of these hints is the correct password?")
                password = input()
                if password not in hints:
                    delay_print("You lose a life for not following directions.")
                    delay_print(f"You could have just chosen {real_hint[0]}....")
                    delay_print(
                        f"You are so very {get_insult(insults)} and you've lost some respect from me."
                    )
                    player.lose_respect()
                    continue
            except IndexError:
                delay_print("There are no possible solutions. You lose a life.")
                delay_print("Listen, I don't make the rules.")
                delay_print(f"Maybe we shouldn't have went to {player.location}...")
                new_random_location = list(pycountry.countries)[
                    random.randint(0, 250)
                ].name
                delay_print(f"Let's go to {new_random_location} instead.")
                player.lose_respect()
                message, password, points, score = begin_round(
                    kanye_quotes, player, location_override=new_random_location
                )

        if password == "quit":
            sys.exit()

        # Check if the password is correct
        if password.lower() not in constants.WORDS:
            delay_print("That's not a real word, at least by my standards.")

            delay_print(
                f"An example of a real word is {random.choice(constants.WORDS)}"
            )
            delay_print(
                "I'm not mad, I'm just dismayed that you're not taking this seriously.",
                color=constants.RED,
            )

            player.lose_respect()
            continue
        # check if the characters in the password are in the location
        if any(char not in player.location.lower() for char in password.lower()):
            delay_print(
                f"You're going to get us killed, {password} isn't in {player.location}!",
                color=constants.RED,
            )
            delay_print("You've lost some respect with me.")
            delay_print("The enemy has intercepted your message.")
            delay_print(
                "They're one step closer to knowing not just our location, but our dignity."
            )
            player.lose_respect()
            continue
        if len(password) != player.level + 3:
            delay_print(
                "You're going to get us canceled by not following instructions!.",
                color=constants.RED,
            )
            delay_print(f"Your password must be {player.level + 3} characters long.")
            delay_print(
                f"The password you entered was {len(password)} characters long."
            )
            delay_print(f"Do you hate {player.location}?")
            delay_print(
                f"You lose a life and the proud people of your {player.location} will never forgive you."
            )
            delay_print("The enemy has intercepted your message.")
            delay_print("They're one step closer to humiliating us.")
            player.lose_respect()
            continue
        cipher = vigenere.Vigenere(key=password).encode(message)
        menu_options(
            "Your encoded message is:",
            cipher,
            "Sending message...",
        )
        # brute force the message by randomly guessing characters
        attempts = player.level * fibonacci(player.level)
        guesser = BruteForceGuesser(
            password, "abcdefghijklmnopqrstuvwxyz", attempts, player.location
        )
        if guesser.guess():
            delay_print("The Vigenere computer guessed your message!")
            delay_print("You lost a life.")
            player.respect -= 1
        else:
            delay_print("The computer failed to guess your message.")
            delay_print("You gained a level.")
            player.level_up()
            player.score += 1 * points * player.level

        delay_print(f"Your score is {score}")
        delay_print(f"You have completed level {str(player.level - 1)}")
        delay_print(f"You have {str(player.respect)} lives left.")
        delay_print(f"You have {str(player.score)} points.")
        new_random_location = list(pycountry.countries)[random.randint(0, 250)].name
        fake_name = fake.name()
        player.location = new_random_location
        player.name = fake_name
        delay_print(
            f"You've moved to {new_random_location}! To further mask your location, you have no choice but to change "
            f"your name to {player.name}. "
        )
        delay_print(f"I like the sound of {player.name} better anyways.")
        delay_print("You have been given a new message to decode.")


def begin_round(kanye_quotes, player, location_override=None):
    if location_override:
        player.location = location_override
    art.tprint(f"Level: {player.level}")
    art.tprint(f"Lives: {player.respect}")
    art.tprint(f"Score: {player.score}")
    delay_print(f"Reputation: {player.adjective}", delay=0)
    delay_print(f"Location: {player.location}", delay=0)
    delay_print(f"Current Name: {player.name}", delay=0)
    # Get a random quote from the Kanye West pandas dataframe
    message = kanye_quotes.sample().iloc[0]["quote"]
    delay_print(
        f"Your {get_insult(insults)}message from {get_insult(insults)}Mr. West is:",
        delay=0.05,
        color=constants.RED,
    )
    delay_print(message, delay=0.05, color=constants.BLUE)
    score = 0
    points = 2
    delay_print(
        f"Choose a {player.level + 3} character password using only the letters from the your current location."
    )
    delay_print("Oh, and it has to also be a real word.")
    delay_print("Press enter to get a hint and lose a point.")
    password = input()
    return message, password, points, score


def instructions(arg0, arg1, arg2):
    delay_print(arg0, delay=0, color=constants.GREEN)
    delay_print(arg1, delay=0, color=constants.GREEN)

    delay_print(arg2, delay=0, color=constants.GREEN)


def menu_options(arg0, arg1, arg2):
    instructions(arg0, arg1, arg2)


if __name__ == "__main__":
    main()
