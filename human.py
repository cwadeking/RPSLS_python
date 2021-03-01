from player import Player


class Human(Player):

    def choose_gesture(self):
        print('Please choose from the following gestures')
        self.print_options()
        user_input = input()
        while user_input != '1' or user_input != '2' or user_input != '3' or user_input != '4' or user_input != '5':
            print('try again')
            user_input = input()

    def print_options(self):
        counter = 0
        for gesture in self.gestures:
            counter += 1
            print(str(counter) + ' ' + gesture)