from game import Game
from human import Human
from computer import Computer

human = Human()

human.choose_gesture()
print(human.chosenGesture)

computer = Computer()
computer.choose_gesture()
print(computer.chosenGesture)