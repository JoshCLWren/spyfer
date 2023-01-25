import sys

from insults import get_insult, insults
from utilities import delay_print


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
