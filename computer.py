from player import Player
from random import Random


class Computer(Player):
    def __init__(self):
        self.name = 'Computer'

    def choose_gesture(self):
        computer_choice = Random.int(0, self.gestures.count())
        print(computer_choice)