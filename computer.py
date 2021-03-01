from player import Player
from random import Random


class Computer(Player):
    # def __init__(self):
    #     super()
    #     self.name = 'Computer'

    def choose_gesture(self):
        length_of_list = len(self.gestures)
        rando = Random()
        computer_choice = rando.randint(0, length_of_list)
        self.chosenGesture = self.gestures[computer_choice]
        print(computer_choice)