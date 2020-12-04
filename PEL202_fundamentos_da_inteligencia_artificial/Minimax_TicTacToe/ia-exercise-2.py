# coding=utf-8
from __future__ import print_function
import copy
import sys
import time


# Implements the Minimax algorithm for tic-tac-toe
class TicTacToe:
    """ TicTacToe Game
    TicTacToe game mode is single player, one player plays against the computer
    """
    # The TicTacToe board is represented as a square matrix of order n, where
    # n is 3.
    BOARD_ORDER = 3
    # The players are X and O, and they are represented as 'X' and 'O' string.
    # An empty position is represented as a string of single space (i.e. ' ').
    PLAYER_X = 'X'
    PLAYER_O = 'O'
    PLAYER_NONE = ' '
    # It is a state that indicates the game is unfinished
    GAME_UNFINISHED = 'unfinished'
    # Represents the maximum value for an int; and INF_2 is the comparison value
    # to determine something is infinite
    INF = sys.maxint
    INF_2 = sys.maxint / 2

    class Action:
        def __init__(self, player, row, column):
            # type: (str, int, int) -> Action
            self.player = player
            self.row = row
            self.column = column

        def __str__(self):
            return self.player \
                   + '(' + str(self.row + 1) \
                   + ', ' + str(self.column + 1) + ')'

    class Board:
        def __init__(self, board=None):
            self.board = \
                self._new_board(TicTacToe.BOARD_ORDER) if not board else board

        def _new_board(self, board_order):
            # The board is represented as a square matrix or order 3.
            return [[TicTacToe.PLAYER_NONE for i in range(board_order)]
                    for j in range(board_order)]

        def actions(self, player):
            # type: (str) -> [Action]
            """ Returns the set of legal moves in a state
            :param player: name of the player to generate the actions
            :return: a list of Actions
            """
            actions = []
            for row in range(len(self.board)):
                for column in range(len(self.board[row])):
                    if self.board[row][column] == TicTacToe.PLAYER_NONE:
                        action = TicTacToe.Action(player, row, column)
                        actions.append(action)
            return actions

        def result(self, action):
            # type: (Action) -> Board
            """ The transition model, which defines the result of a move
            :param action: actions to act upon the board
            :return: return a new version of the Board
            """
            n_board = copy.deepcopy(self.board)
            n_board[action.row][action.column] = action.player
            return TicTacToe.Board(n_board)

        def is_action_valid(self, action):
            # type: (Action) -> Boolean
            """ Is action valid?
            :param action: Action to be validated against this Board
            :return: True if the action is valid, otherwise False
            """
            row = action.row
            column = action.column
            if 0 <= row < len(self.board) and 0 <= column < len(self.board):
                if self.board[row][column] == TicTacToe.PLAYER_NONE:
                    return True
            return False

        def player(self, row, column):
            """ Get the Player that is in the position of row and column
            :param row: board row
            :param column: board column
            :return: the player in the row and column position
            """
            return self.board[row][column]

        def is_full(self):
            # type: () -> Boolean
            """ Is board full?
            :return: True if the board is full, otherwise is False
            """
            return not any(self.board[row][column] == TicTacToe.PLAYER_NONE
                           for row in range(len(self))
                           for column in range(len(self)))

        def __len__(self):
            return len(self.board)

        def __str__(self):
            return '\n'.join([' | '.join(line) for line in self.board])

    class Minimax:
        def __init__(self, level_limit=2):
            self.level_limit = level_limit

        def decision(self, board, player):
            # type: (Board, str) -> Action
            """ Decide which action to take for a player in a board
            :param board: the board to apply the minimax algorithm
            :param player: the player to make an action decision
            :return: the decided action
            """
            v, action = self._max_value(board, player, 0)
            return action

        def _max_value(self, board, player, level):
            # type: (Board, str, int) -> int, Action
            if self.is_terminal(board) or level >= self.level_limit:
                return self.utility(board, player), \
                       TicTacToe.Action(player, None, None)

            minimax_v = -2 * TicTacToe.INF
            minimax_action = None
            for action in board.actions(player):
                work_board = board.result(action)
                v, other_action, = self._min_value(
                    work_board,
                    player,
                    level + 1)
                if v > minimax_v:
                    minimax_v = v
                    minimax_action = action
            return minimax_v, minimax_action

        def _min_value(self, board, player, level):
            # type: (Board, str, int) -> int, Action
            if self.is_terminal(board) or level >= self.level_limit:
                return self.utility(board, player), \
                       TicTacToe.Action(player, None, None, )

            minimax_v = 2 * TicTacToe.INF
            minimax_action = None
            for action in board.actions(TicTacToe.opponent(player)):
                work_board = board.result(action)
                v, other_action, = self._max_value(
                    work_board,
                    player,
                    level + 1)
                if v < minimax_v:
                    minimax_v = v
                    minimax_action = action
            return minimax_v, minimax_action,

        def utility(self, board, player):
            """ Minimax utility function
            The utility function for TicTacToe considers the number of
            possibilities to win the game.
            A positive value means the player has more chances to win. If the
            utility returns a value greater than INF_2 means that the player
            has won, and a value lower than -INF_2 the opponent has won.

            :param board: the Board runs the utility against
            :param player: the player to maximize the utility
            :return: A numeric value for a game. If positive, player has more
            chances to win.
            """
            player_positions = {
                TicTacToe.PLAYER_X: [0 for i in range(4)],
                TicTacToe.PLAYER_O: [0 for i in range(4)],
                TicTacToe.PLAYER_NONE: [0 for i in range(4)],
            }
            utilities = {
                TicTacToe.PLAYER_X: 0,
                TicTacToe.PLAYER_O: 0,
            }
            board_order = len(board)

            def _compute_utilities(pos):
                for c_player in utilities:
                    c_opponent = TicTacToe.opponent(c_player)
                    if player_positions[c_player][pos] == board_order:
                        utilities[c_player] = TicTacToe.INF
                    else:
                        c_opponent_presence = player_positions[c_opponent][pos]
                        if c_opponent_presence == 0:
                            utilities[c_player] += 1

            for i in range(board_order):
                for positions in player_positions.values():
                    positions[0] = 0
                    positions[1] = 0

                for j in range(board_order):
                    # Row
                    by_row = board.player(i, j)
                    player_positions[by_row][0] += 1
                    # Column
                    by_column = board.player(j, i)
                    player_positions[by_column][1] += 1
                    # Diagonal
                    if i == j:
                        by_diagonal = board.player(i, j)
                        player_positions[by_diagonal][2] += 1
                    # Inverted diagonal
                    if i == board_order - j - 1:
                        by_inv_diagonal = board.player(i, j)
                        player_positions[by_inv_diagonal][3] += 1

                # Adjust utility according to the row and column
                _compute_utilities(0)
                _compute_utilities(1)

            # Adjust utility according to the diagonals
            _compute_utilities(2)
            _compute_utilities(3)

            opponent = TicTacToe.opponent(player)
            return utilities[player] - utilities[opponent]

        def is_terminal(self, board):
            """ Is terminal state?
            :param board: Board that represent the state
            :return: True if the state is terminal, otherwise False
            """
            board_full = board.is_full()
            v = self.utility(board, TicTacToe.PLAYER_X)
            return any([board_full, abs(v) >= TicTacToe.INF_2])

    def __init__(self):
        self.board = TicTacToe.Board()
        self.minimax = TicTacToe.Minimax()
        # Player X is the first one to move
        self.turn = TicTacToe.PLAYER_X

    @staticmethod
    def opponent(player):
        return TicTacToe.PLAYER_X if player == TicTacToe.PLAYER_O \
                                  else TicTacToe.PLAYER_O

    def _find_winner(self):
        if not self.minimax.is_terminal(self.board):
            return TicTacToe.GAME_UNFINISHED
        v = self.minimax.utility(self.board, TicTacToe.PLAYER_X)
        if abs(v) < self.INF_2:
            return self.PLAYER_NONE
        return self.PLAYER_X if v > self.INF_2 else self.PLAYER_O

    def _get_user_option(self, player):
        options = ', '.join([str(i + 1) for i in range(TicTacToe.BOARD_ORDER)])
        row = input("Enter the row (" + options + "): ")
        column = input("Enter the column (" + options + "): ")
        return TicTacToe.Action(player, row - 1, column - 1)

    def _print_game_header(self):
        print('\n')
        print('-' * 80)
        print('TicTacToe\n')
        print(str(self.board))

    @staticmethod
    def _same_math_sign(a, b):
        return True if abs(a + b) == abs(a) + abs(b) else False

    def play(self):
        # type: () -> None
        """ Play 1 game against the computer
        """
        print('Welcome!')
        print("You're the player " + self.turn)
        while self._find_winner() == TicTacToe.GAME_UNFINISHED:
            self._print_game_header()
            print('Turn: ' + self.turn + '\n')

            action = None
            if self.turn == TicTacToe.PLAYER_X:
                action = self._get_user_option(self.turn)
            else:
                print('Processing...')
                time.sleep(1)
                action = self.minimax.decision(self.board, self.turn)

            if self.board.is_action_valid(action):
                self.board = self.board.result(action)
                self.turn = self.opponent(self.turn)
            else:
                print('Invalid position!!!')

        winner = self._find_winner()
        self._print_game_header()
        print('\n' + 'RESULT: ' + ('draw' if winner == TicTacToe.PLAYER_NONE
                                   else 'player ' + winner + ' won!'))


def main():
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()