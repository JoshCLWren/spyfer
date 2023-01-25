import random

from main import fake
from puzzle import possible_words
from utilities import delay_print


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
