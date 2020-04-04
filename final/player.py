import sys
from DotsAndBoxes import *
import random
def simple_player(game):
    move_list = game.getmovelist()
    smallest = 1000
    for i in range(0,game.r):
        for j in range(0,game.c):
            if i%2!=0 and j%2!=0 and game.board[i,j] == 0:
                if game.check_fill_move(i,j):
                    return game.check_fill_move(i,j)  
                elif check_double_lines(i,j):
                    a,b = check_double_lines(i,j)
                    move_list.pop(a,b) 
    if move_list is not []:
        return random.choice(move_list)
    else:
        move_list = game.getmovelist()
    for move in move_list:
        newgame = game._copy(game)
        if newgame.check_fill_move(move[0],move[1]):
            num = cal_filled_all()
            if num < smallest:
                bestmove = move
    return bestmove
def mid_player(game):
    move_list = game.getmovelist()
    smallest = 1000
    for i in range(0,game.r):
        for j in range(0,game.c):
            if i%2!=0 and j%2!=0 and game.board[i,j] == 0:
                if game.check_fill_move(i,j):
                    return game.check_fill_move(i,j)                  
                if check_double_lines(i,j):
                    a,b = check_double_lines(i,j)
                    move_list.pop(a,b) 
    if move_list is not []:
        return random.choice(move_list)    
    if move_list is []:
        move_list = game.getmovelist()
    score, move = minmax(game)    
    return move
def high_player(game):
    move_list = game.getmovelist()
    for i in range(0,game.r):
        for j in range(0,game.c):
            if i%2!=0 and j%2!=0 and game.board[i,j] == 0:
                if check_double_lines(i,j):
                    a,b = check_double_lines(i,j)
                    move_list.pop(a,b) 
    for i in range(0,game.r):
        for j in range(0,game.c):
            if i%2!=0 and j%2!=0 and game.board[i,j] == 0:
                if game.check_fill_move(i,j) and move_list is not []:
                    return game.check_fill_move(i,j) 
    return aplhabeta(newgame,dic,aplah,beta,"Max")[1]
def aplhabeta(game,dic,alpha,beta,minOrMax):
    if game.is_over():
        player_score = game.score[game.turn == 1]
        opponent_score = game.score[game.turn == -1]
        dic[game.board.tobytes()] = player_score - opponent_score
        dic[np.flipud(game.board).tobytes()] = player_score - opponent_score
        dic[np.flip(game.board).tobytes()] = player_score - opponent_score
        dic[np.fliplr(game.board).tobytes()] = player_score - opponent_score
        return player_score - opponent_score, None
    if game.board.tobytes() in dic:
        return dic[game.board.tobytes()],None
    if minOrMax == Max:
        v = -1000
        move_list = game.getmovelist()
        best_move, best_score = available_moves[0], v
        for move in move_list:
            newgame = game._copy(game)
            newgame.play(move)
            if newgame.turn == game.turn:
                v = max(v, aplhabeta(newgame,dic,aplah,beta,"Max")[0])
            else:
                v = max(v, aplhabeta(newgame,dic,aplah,beta,"Min")[0])
            if v > best_score:
                best_move = move
                best_score = v
            aplah = max(aplah, v)
            if beta <= aplah:
                break
        dic[game.board.tobytes()] = v
        dic[np.flipud(game.board).tobytes()] = v
        dic[np.flip(game.board).tobytes()] = v
        dic[np.fliplr(game.board).tobytes()] = v        
        return v, best_move
    else:
        v = 1000
        move_list = game.getmovelist()
        best_move, best_score = available_moves[0], v
        for move in move_list:
            newgame = game._copy(game)
            newgame.play(move)
            if newgame.turn == game.turn:
                v = min(v, aplhabeta(newgame,dic,aplah,beta,"Min")[0])
            else:
                v = min(v, aplhabeta(newgame,dic,aplah,beta,"Max")[0])
            if v < best_score:
                best_move = move
                best_score = v
            beta = min(beta, v)
            if beta <= alpha:
                break
        dic[game.board.tobytes()] = v
        dic[np.flipud(game.board).tobytes()] = v
        dic[np.flip(game.board).tobytes()] = v
        dic[np.fliplr(game.board).tobytes()] = v          
        return v, best_move    
        
def minmax(game, player):
    if game.is_over():
        player_score = game.score[player == 1]
        opponent_score = game.score[player == -1]
        return player_score - opponent_score,None
    move_list = game.getmovelist()
    minscore = 1000
    maxscore = -1000
    if game.turn == 1:
        for move in move_list:
            newgame = game._copy(game)
            newgame.play(move)
            score,thisMove = minmax(newgame,newgame.turn)
            if score > maxscore:
                maxscore = max(maxscore,score)
                bestmove = thisMove
        return so_far,bestmove
    if game.turn == -1:
        for move in move_list:
            newgame = game._copy(game)
            newgame.play(move)
            score,thisMove = minmax(newgame,newgame.turn)
            if score < minscore:
                minscore = min(miniscore, score)
                bestmove = thisMove
        return so_far,bestmove    

            
    
    

def cal_filled_all(game,move):
    gameon = game.copy()
    filledNum = 1 
    gameon.play(move)
    while True:
        move = gameon.check_fill_move()
        if move != None:
            gameon.play(move)
            filledNum += 1
        else:
            break
    return filledNum




def not_third_line(game):
    move_list = valid_moves()
    for i in range(0,game.r):
        for j in range(0,game.c):
            if i%2!=0 and j%2!=0:
                if check_double_lines(i,j):
                    a,b = check_double_lines(i,j)
                    move_list.pop(a,b)

    return move_list

def max_score(game):
    init_game = game._copy(game)
    chk = True
    while chk == True:
        move_list = valid_moves()
        fill_move =[]
        made_moves = []
        score = 0
        for i in range(0,game.r):
            for j in range(0,game.c):
                if i%2==0 and j%2==0:
                    if i%2==0 and j%2==0:
                        if check_fill_move(i,j):
                            fill_move.append(check_fill_move(i,j))
        if not fill_move:
            chk = False
        else:
            for move in fill_move:
                made_moves.append(move_list.pop(i))
                score += 1
                game.play(move)
    game = init_game
    return score, made_moves

def pick_double_move(game):
    move_list = valid_moves()
    current_score = 100
    score = 0
    current_moves = []
    moves = []
    picked_move = ()
    init_game = game._copy(game)
    for move in move_list:
        game.play(move)
        score,moves = max_score(game)
        if score < current_score:
            current_score = score
            current_moves = moves
            picked_move = move
        game = init_game()
    return picked_move
