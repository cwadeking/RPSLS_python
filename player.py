from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        self.name = ''
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.chosenGesture = ''

    @abstractmethod
    def choose_gesture(self):
        pass