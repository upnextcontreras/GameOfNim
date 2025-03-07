from games import *  # This will important the classes from game and gamestate  

class GameOfNim(Game):
    def __init__(self, board=[3, 1]):
        board = [int(x) if not isinstance(x, int) and isinstance(x, tuple) else x for x in board] #  Make sure the that any tuple factor will become an int
        self.initial = GameState(to_move="MAX", utility=0, board=board, moves=self.compute_moves(board)) # Initalize the gamestate and gives the allowed moves by board

    def compute_moves(self, board):
        moves = []
        # Iterate over each row (i) and its object count.
        for i, count in enumerate(board): # will iterate each row and object 
            for n in range(1, count + 1): # basically each removal n from 1 add the move (i,n)
                moves.append((i, n))
        return moves

    def actions(self, state):
        return state.moves # returns the moves of the state

    def result(self, state, move):
        r, n = move
        new_board = list(map(lambda x: x if isinstance(x, int) else x[0], state.board)) # will covert elements of board to int(stored as tuple)
        new_board[r] -= n # subtracts n objects from r rows

        new_player = "MIN" if state.to_move == "MAX" else "MAX" # switches from MAX and MIN turns
        new_moves = self.compute_moves(new_board) # plays new allowed moves from new board
        is_terminal = sum(new_board) == 0 # will check if new board is done
        if is_terminal:
            utility = 1 if new_player == "MAX" else -1 # if board empty the mover loses so next player is the winner
        else:
            utility = 0

        # Return a new GameState with the updated board, player, utility, and moves.
        return GameState(to_move=new_player, utility=utility, board=new_board, moves=new_moves)

    def terminal_test(self, state):
        board_values = [x if isinstance(x, int) else x[0] for x in state.board]
        return sum(board_values) == 0 # return true if board is empty which is done by summing object counts

    def utility(self, state, player):
        if player == "MAX": # returns the utility state  of player 
            return state.utility
        else:
            return -state.utility # if min the sign is inverted

    def display(self, state):
        print("board:", state.board) # prints board

    def play_game(self, computer, human):
        state = self.initial
        print("board:", state.board)  # displays the initial board.
        while True:
            move = computer(self, state)  # computer move 
            print(move)  
            state = self.result(state, move)  # updates based on move
            self.display(state)  
            if self.terminal_test(state): # if game is done then display winner
                print("MAX won the game" if state.utility > 0 else "MIN won the game")
                return state.utility
            
            print("current state: board:", state.board) # displays board, available move, and allows for move to be made
            print("available moves:", state.moves)
            print("\nYour move?", end=" ")  
            
            move = human(self, state)  # player's move.
            print(move)  
            state = self.result(state, move)  # updates based on move
            self.display(state)  
            if self.terminal_test(state): # if game is done then display winner
                print("MAX won the game" if state.utility > 0 else "MIN won the game")
                return state.utility

def query_player(game, state):
    move_string = input()
    try:
        move_string = move_string.strip() # removes whitespace/parentheses
        if move_string.startswith('(') and move_string.endswith(')'):
            move_string = move_string[1:-1]
    
        parts = move_string.split(',') # splits the input by a comma and make it a int
        row = int(parts[0])
        num = int(parts[1])
        move = (row, num)
    except:
        print('Invalid move. Please enter in format (row,number) (e.g., "(0,1)")')
        return query_player(game, state)
    
    if move not in game.actions(state):# checks if move is allowed or avaiable 
        print('Illegal move. Please try again.')
        return query_player(game, state)
    return move

if __name__ == "__main__": # create initial board while using alpha(computer) and query(human)
    nim = GameOfNim(board=[7, 5, 3, 1])
    nim.play_game(alpha_beta_player, query_player)
