"""
main.py

"""

from human_player import HumanPlayer
from computer_player import ComputerPlayer
from hexapawn_game import HexapawnGame

def game_setup(player):
    while True:
        user_input = input(f'\nIs player {player} a human? (y/n): ')
        if user_input == 'q':
            exit()
        elif user_input == 'y':
            print(f'Player {player} is a human.\n')
            return HumanPlayer(input(f'What is player {player}\'s name?: '))
        elif user_input == 'n':
            print(f'Player {player} is a computer.\n')
            name = input(f'What is player {player}\'s name?: ')
            strategy = input(f'What is player {player}\'s strategy?: ')
            return ComputerPlayer(name, strategy)
        else:
            print('Invalid input. Enter y, n, or q.')


player1 = game_setup(1)
player2 = game_setup(2)

game = HexapawnGame(player1, player2)
print('\nStarting game...\n')
game.play()