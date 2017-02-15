"""Ping Pong Game"""


class Pong:
    def __init__(self, name):
        self.point = 0
        self.name = name

    @classmethod
    def input_check(cls, input_value):
        hit_list = ['h', 'H']

        if input_value in hit_list:
            return True
        else:
            return False

    @classmethod
    def game(cls, player):
        while player[0].point is not 11:
            print('\n%s\'s serve:' % player[0].name)
            while True:
                user_input = raw_input()
                if Pong.input_check(user_input):
                    player = list(reversed(player))
                    print(player[0].name + '\'s turn:')
                elif not Pong.input_check(user_input):
                    print(player[1].name + ' got a point\n')
                    player = list(reversed(player))
                    player[0].point += 1
                    break
            print('%s\'s point: %d' % (player[0].name, player[0].point))
            print('%s\'s point: %d' % (player[1].name, player[1].point))

        print('\n\t\t\t' + player[0].name + ' won ')


if __name__ == '__main__':
    player1 = Pong(raw_input('Enter player1 name\n'))
    player2 = Pong(raw_input('Enter player2 name\n'))

    player_list = [player1, player2]

    print('\n\nInstructions: Press H or h to hit and D or d for drop ')
    print('Any other entry rather than given options will be considered as '
          'drop')
    print('\n\t\tGame begins\t\n\n')

    Pong.game(list(player_list))

