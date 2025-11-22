"""
main.py

NOTES:
    figure out a better way to load an agent while maintaining project separation.
    make it cleaner to easily run repeatedly with no user input (to train models)
"""
import os
import sys
import importlib.util
from human_player import HumanPlayer
from computer_player import ComputerPlayer
from board import Board
from hexapawn_game import HexapawnGame

# AGENT_REGISTRY = {
#     'menace': Menace
#     #'custom': MyCustomAgent,  # add agents here
# }


def load_agent_from_file(agent_file_path: str, class_name: str, dependencies=None):
    """
    Load a Python class from any file path.

    Args:
        agent_file_path (str): Absolute path to the .py file containing the agent class
        class_name (str): Name of the class in that file

    Returns:
        The class object (can be instantiated later)
    """
    if not os.path.exists(agent_file_path):
        raise FileNotFoundError(f"Agent file not found: {agent_file_path}")

    spec = importlib.util.spec_from_file_location(class_name, agent_file_path)
    module = importlib.util.module_from_spec(spec)

    if dependencies:
        for name, obj in dependencies.items():
            setattr(module, name, obj)

    spec.loader.exec_module(module)

    return getattr(module, class_name)


def load_agent_class(file_path, class_name):
    folder = os.path.dirname(file_path)
    sys.path.insert(0, folder)  # temporarily add folder to path

    module_name = os.path.splitext(os.path.basename(file_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    cls = getattr(module, class_name)

    sys.path.pop(0)  # remove folder from path
    return cls


def generate_states():
    """
    Generates possible game states and legal moves from each state.

    Returns:
         states_and_moves (dict): Maps game states to legal moves.
    """
    board = Board()
    states_and_moves = {}
    state_generator(states_and_moves, board)

    return states_and_moves


def state_generator(states_and_moves, board, curr_player=1):
    """
    Game can only start with player 1.

    Args:
        states_and_moves (dict): Maps game states to legal moves.
        board (Board): The board.
        curr_player (int): The player whose turn it is.
    """
    board_str = board.to_string()

    if board_str in states_and_moves:
        return  # already visited

    legal_moves = board.get_legal_moves(curr_player)
    states_and_moves[board_str] = legal_moves

    for move in legal_moves:
        next_board = board.copy()
        next_board.move_piece(*move)
        next_player = 2 if curr_player == 1 else 1
        state_generator(states_and_moves, next_board, next_player)


def player_setup(player_position, states_and_moves=None, model_path=None):
    """
    Gets user input and sets up players.
    """
    command_line = False

    if command_line is True:
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
                # strategy = input(f'What is player {player_position}\'s strategy?: ')
                # model_class = AGENT_REGISTRY.get(strategy)

                base_dir = os.path.dirname(os.path.abspath(__file__))  # this directory
                rel_file_path = os.path.join(base_dir, '../AI-Practice/reinforcement/MENACE/menace.py') # syntax might not work on Windows

                # abs_file_path = '/Users/......./MENACE/menace.py'

                agent_file = rel_file_path  # change this to select relative or absolute and comment out one of the lines above
                model_class = load_agent_class(agent_file, "Menace")

                states_and_moves = generate_states()

                info = {
                    'player_position': player_position,
                    'game_name': 'hexapawn',
                    'states_and_moves': states_and_moves
                }

                selected_model = None
                if model_class:
                    selected_model = model_class(**info)

                return ComputerPlayer(name, selected_model)
            else:
                print('Invalid input. Enter y, n, or q.')
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))  # this directory
        rel_file_path = os.path.join(base_dir, '../AI-Practice/reinforcement/MENACE/menace.py') # syntax might not work on Windows

        # abs_file_path = '/Users/......./MENACE/menace.py'

        agent_file = rel_file_path # change this to select relative or absolute and comment out one of the lines above
        model_class = load_agent_class(agent_file, "Menace")

        states_and_moves = generate_states()

        info = {
            'player_position': player_position,
            'game_name': 'hexapawn',
            'states_and_moves': states_and_moves
        }

        selected_model = None
        if model_class:
            selected_model = model_class(**info)

        return ComputerPlayer(f'player{player_position}', selected_model)


def game_setup(board=None, start_player=None):
    """
    Sets up a new game.

    Args:
        board (Board): A game board. Optional if starting a new game.
        start_player (int): The player whose move it is. Optional if starting a new game.

    Returns:
        (HexapawnGame): A game.
    """
    player1 = player_setup(1)
    player2 = player_setup(2)

    if board is None:
        return HexapawnGame(player1, player2)
    else:
        return HexapawnGame(player1, player2, board, start_player)


def main():

    for _ in range(100):
        generate_states()

        # MenaceClass = load_agent_from_file("/path/to/menace.py", "Menace")
        #
        # for path, cls_name in external_agents:
        #     cls = load_agent_from_file(path, cls_name)
        #     AGENT_REGISTRY[cls_name.lower()] = cls

        #board = Board(3, '222010101')
        #game = game_setup(board, 2)
        game = game_setup()

        print('\nStarting game...\n')
        game.play()


if __name__ == "__main__":
    main()