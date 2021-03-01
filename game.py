from human import Human


class Game:
    def __init__(self):
        # self.playerOne
        # self.playerTwo
        self.roundNumber = 0
        # self.decide_number_of_rounds()

    def decide_number_of_rounds(self):
        print('After how many round wins will a player be declared a winner?')
        self.roundNumber = input()
        print(self.roundNumber)

    def test_human_choose(self):
        player_one = Human()
        player_one.choose_gesture()