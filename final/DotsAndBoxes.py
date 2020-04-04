import numpy as np

PLAYER1 = -1
PLAYER2 = 1
PLAYERS = {'B': -1, 'W': 1}

def board_shape(board_string):
    lines = board_string.split("|")
    rows, cols = (len(lines)+1)/2, (len(lines[0])+1)/2
    return rows, cols

class DotsAndBoxes(object):
    def __init__(self, initial_player=None, rows=None, cols=None, board_string=None, game_obj=None):
        if board_string is not None: # construct from string
            self._from_string(initial_player, board_string)
        elif game_obj is not None:   # copy constructor
            self._copy(game_obj)
        else:
            self.rows, self.cols = rows, cols
            self.score = [0, 0] # B, W
            self.turn = initial_player
            self.board = np.zeros((2*rows-1, 2*cols-1), dtype=np.int)
            self.r, self.c = self.board.shape
            self.num_boxes = (rows-1) * (cols-1)

    def _from_string(self, initial_player, board_string):
        lines = board_string.split("|")
        rows, cols = board_shape(board_string)
        self.__init__(initial_player, rows, cols)
        for i, r in enumerate(lines):
            for j, s in enumerate(r):
                edge, box = i%2 != j%2, i%2 == j%2 == 1
                if edge and s == 'x':      # is a filled edge
                    self.board[i, j] += 1
                elif box and s in PLAYERS: # is a filled box
                    self.board[i, j] = PLAYERS[s]
                    self.score[PLAYERS[s] == 1] += 1

    def _copy(self, game_obj):
        self.__dict__.update(game_obj.__dict__)
        self.board = np.array(game_obj.board)
        self.score = game_obj.score[:]

    def play(self, move=None, i=None, j=None, player=None):
        if not player:
            player = self.turn
        if move is not None:
            i, j = move
        if self._is_valid(player, i, j):
            self.board[i, j] = player
            self._update(player, i, j)

    def getmovelist(self):
        move_list=[]
        for r in range(2*self.rows-1):
            for c in range(2*self.cols-1):
                if self.board[r,c] == 0 and r%2 != c%2:
                    move_list.append((r,c))
        return move_list
    def _is_valid(self, player, i, j):
        return self.turn == player and self.board[i, j] == 0 and i%2 != j%2 and not self.is_over()

    def is_over(self):
        return sum(self.score) == self.num_boxes

    def _update(self, player, i, j):
        vertical = i%2 > j%2
        a = self._check_box(player, i, j-1) if vertical else self._check_box(player, i-1, j)
        b = self._check_box(player, i, j+1) if vertical else self._check_box(player, i+1, j)
        if not (a or b): # did not fill any box
            self.turn *= -1

    def _check_box(self, player, i, j):
        if (i and i < self.r) and (j and j < self.c):
            filled = self.board[i-1, j] and self.board[i+1, j] and self.board[i, j-1] and self.board[i, j+1]
            if filled:
                self.board[i, j] = player
                self.score[player == 1] += 1
            return filled
    def get_board(self):
        return self.board
    
    def check_fill_move(self):
        for i in range(2*self.rows-1):
            for j in range(2*self.cols-1):
                if i%2 != 0 and j%2 != 0:
                    if  self.board[i,j] == 0 and self.board[i-1, j] != 0  and self.board[i+1, j] != 0 and self.board[i, j-1] != 0:
                        return (i, j+1)
                    elif  self.board[i,j] == 0 and self.board[i-1, j] != 0 and self.board[i+1, j] != 0 and self.board[i, j+1] != 0:
                        return (i, j-1)
                    elif  self.board[i,j] == 0 and self.board[i, j-1] != 0 and self.board[i-1, j] != 0 and self.board[i, j+1] != 0:
                        return (i+1, j)
                    elif  self.board[i,j] == 0 and self.board[i, j-1]!= 0 and self.board[i+1, j] != 0 and self.board[i, j+1]  != 0:
                        return (i-1, j)

        return None  
    

    def check_two_lines(self,i,j):
        filled = self.board[i-1, j] and self.board[i+1, j] and self.board[i, j-1] and self.board[i, j+1]
        if filled:
            return None
        
        if self.board[i-1, j] and self.board[i+1, j] and self.board[i, j-1]:
            return None
        elif self.board[i-1, j] and self.board[i+1, j] and self.board[i, j+1]:
            return None
        elif self.board[i, j-1] and self.board[i+1, j] and self.board[i, j+1]:
            return None
        elif self.board[i, j-1] and self.board[i+1, j] and self.board[i, j+1]:
            return None
    
        if self.board[i-1, j] and self.board[i+1, j]:
            return (i, j-1) ,(i, j+1)
        elif self.board[i-1, j] and self.board[i, j-1]:
            return (i+1, j),(i, j+1)
        elif self.board[i-1, j] and self.board[i, j+1]:
            return (i+1, j),(i, j-1)
        elif self.board[i+1, j] and self.board[i, j-1]:
            return (i-1, j),(i, j+1)
        elif self.board[i+1, j] and self.board[i, j+1]:
            return (i-1, j),(i, j-1)
        elif self.board[i, j-1] and self.board[i, j+1]:
            return (i-1, j),(i+1, j)
        else:
            return None
    def check_empty_lines(self):
        lis = []
        for i in range(self.r):
            for j in range(self.c):
                if i%2 != j%2 and self.board[i,j] == 0:
                    lis.append((i,j))
                        
        for i in range(self.r):
            for j in range(self.c):
                if i%2 != 0 and j%2 != 0:
                    if  self.board[i-1, j] != 0 or self.board[i+1, j] != 0 or self.board[i, j-1] != 0 or self.board[i, j+1] != 0:
                        if (i-1, j) in lis:
                            lis.remove((i-1, j))
                        if (i+1, j) in lis:
                            lis.remove((i+1, j))
                        if (i, j-1) in lis:
                            lis.remove((i, j-1))
                        if (i, j+1) in lis:
                            lis.remove((i, j+1))
        return lis


