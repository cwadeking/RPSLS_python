from player import Player


class Human(Player):

    def choose_gesture(self):
        self.print_options()
        gesture_number = self.gather_input_from_user()
        self.chosen_gesture = self.gestures[gesture_number - 1]

    def print_options(self):
        print('Please choose from the following gestures')
        counter = 0
        for gesture in self.gestures:
            counter += 1
            print(str(counter) + ' ' + gesture)

    def gather_input_from_user(self):
        user_input = input()
        while user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4' and user_input != '5':
            print('try again')
            user_input = input()
        return int(user_input)