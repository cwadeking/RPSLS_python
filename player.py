from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        self.name = ''
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.chosen_gesture = ''
        self.score = 0

    @abstractmethod
    def choose_gesture(self):
        pass