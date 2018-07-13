import random

class Coin:
    def __init__(self):
        self.states = ['H', 'T']

    def flip (self):
        return random.choice(self.states)