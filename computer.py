from player import Player
from random import Random


class Computer(Player):
    # def __init__(self):
    #     super()
    #     self.name = 'Computer'

    def choose_gesture(self):
        length_of_list = len(self.gestures)
        random_number = Random()
        computer_choice = random_number.randint(0, length_of_list - 1)
        self.chosen_gesture = self.gestures[computer_choice]
        print(computer_choice)