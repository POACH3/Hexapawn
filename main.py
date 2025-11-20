"""
main.py

"""
import os
import sys
import csv
from human_player import HumanPlayer
from computer_player import ComputerPlayer
from board import Board
from hexapawn_game import HexapawnGame
from menace import Menace

MODEL_REGISTRY = {
    'menace': Menace
}

menace_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../MENACE'))
sys.path.append(menace_path)

def generate_states():
    """
    Generates possible game states. MENACE must know all states in advance in
    order to initialize the matchboxes for each state.

    NOTES:
         remove csv writing
         return a dict of (state, legal_moves)
    """
    board = Board()
    player_position = 1

    game_states = state_generator(board, player_position)
    initial_beads = '3'

    # write to CSV
    with open('hexapawn_menace_model.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # write each board string as a row
        for state_str in sorted(game_states):
            writer.writerow([state_str, initial_beads])


def state_generator(board, player, all_states=None):
    if all_states is None:
        all_states = set()

    legal_moves = board.get_legal_moves(player)

    if len(legal_moves) != 0:
        for move in legal_moves:
            next_board = board.copy()
            next_board.move_piece(*move)

            if next_board.to_string() not in all_states:
                all_states.add(next_board.to_string())

                # change player
                next_player = 2 if player == 1 else 1

                # go to each new state, but check if win before trying to go to new state
                state_generator(next_board, next_player, all_states)

    return all_states


def player_setup(player_position):
    """
    Gets user input and sets up players.
    """
    while True:
        user_input = input(f'\nIs player {player_position} a human? (y/n): ')
        if user_input == 'q':
            exit()
        elif user_input == 'y':
            print(f'Player {player_position} is a human.\n')
            return HumanPlayer(input(f'What is player {player_position}\'s name?: '))
        elif user_input == 'n':
            print(f'Player {player_position} is a computer.\n')
            name = input(f'What is player {player_position}\'s name?: ')
            strategy = input(f'What is player {player_position}\'s strategy?: ')
            model_class = MODEL_REGISTRY.get(strategy)

            selected_model = None
            if model_class:
                selected_model = model_class('hexapawn', player_position)

            return ComputerPlayer(name, selected_model)
        else:
            print('Invalid input. Enter y, n, or q.')


def game_setup(board=None):
    """
    Sets up a new game.

    Args:
        board (Board): A game board.

    Returns:
        (HexapawnGame): A new game.
    """
    player1 = player_setup(1)
    player2 = player_setup(2)

    if board is None:
        return HexapawnGame(player1, player2)
    else:
        return HexapawnGame(player1, player2, board)
    

def main():

    #generate_states()
    game = game_setup()

    print('\nStarting game...\n')
    game.play()


if __name__ == "__main__":
    main()