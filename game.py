from human import Human
from computer import Computer

class Game:
    def __init__(self):
        self.roundNumber = 0
        self.player_one = None
        self.player_two = None

    def decide_number_of_rounds(self):
        print('After how many round wins will a player be declared a winner?')
        self.roundNumber = int(input())

    def run_game(self):
        player_mode = self.pick_player_mode()
        self.player_creator(player_mode)
        self.decide_number_of_rounds()
        while self.player_one.score < self.roundNumber and self.player_two.score < self.roundNumber:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.compare_gestures()
        self.display_winner()

    def pick_player_mode(self):
        print('Please select what type of game you want to play.')
        print('Press 1 for single player, and press 2 for multiplayer')
        user_input = input()
        while user_input != '1' and user_input != '2':
            print('try again')
            user_input = input()
        return int(user_input)

    def player_creator(self, choice):
        if choice == 1:
            self.player_one = Human()
            self.player_two = Computer()
        elif choice == 2:
            self.player_one = Human()
            self.player_one = Human()

    def compare_gestures(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print('nothing happens.  Its a draw')
        elif self.player_one.chosen_gesture == 'rock':
            if self.player_two.chosen_gesture == 'paper' or self.player_two.chosen_gesture == 'spock':
                self.player_two.score += 1
                print('player two wins')
            else:
                self.player_one.score += 1
                print('player one wins')
        elif self.player_one.chosen_gesture == 'paper':
            if self.player_two.chosen_gesture == 'scissors' or self.player_two.chosen_gesture == 'lizard':
                self.player_two.score += 1
                print('player two wins')
            else:
                self.player_one.score += 1
                print('player one wins')
        elif self.player_one.chosen_gesture == 'scissors':
            if self.player_two.chosen_gesture == 'rock' or self.player_two.chosen_gesture == 'spock':
                self.player_two.score += 1
                print('player two wins')
            else:
                self.player_one.score += 1
                print('player one wins')
        elif self.player_one.chosen_gesture == 'lizard':
            if self.player_two.chosen_gesture == 'rock' or self.player_two.chosen_gesture == 'scissors':
                self.player_two.score += 1
                print('player two wins')
            else:
                self.player_one.score += 1
                print('player one wins')
        elif self.player_one.chosen_gesture == 'spock':
            if self.player_two.chosen_gesture == 'paper' or self.player_two.chosen_gesture == 'lizard':
                self.player_two.score += 1
                print('player two wins')
            else:
                self.player_one.score += 1
                print('player one wins')

    def display_winner(self):
        if self.player_one.score == self.roundNumber:
            print('player one wins the game')
        else:
            print('player two wins the game')