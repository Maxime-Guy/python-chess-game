from copy import deepcopy

class AI:
    def __init__(self, depth=3):
        self.depth = depth

    def get_best_move(self, board, color):
        evaluation, best_move = self.minimax(
            board, self.depth, float('-inf'), float('inf'), True, color)
        return best_move

    def minimax(self, board, depth, alpha, beta, maximizing_player, color):
        if depth == 0 or board.is_checkmate(color) or board.is_stalemate(color):
            return self.evaluate_board(board), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in board.get_all_moves(color):
                board_copy = board.copy()
                board_copy.move_piece(move)
                evaluation = self.minimax(
                    board_copy, depth - 1, alpha, beta, False, 'black' if color == 'white' else 'white')[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in board.get_all_moves(color):
                board_copy = board.copy()
                board_copy.move_piece(move)
                evaluation = self.minimax(
                    board_copy, depth - 1, alpha, beta, True, 'black' if color == 'white' else 'white')[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return min_eval, best_move
