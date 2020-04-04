import pygame
import numpy as np
from DotsAndBoxes import *
import sys
from DotsAndBoxes import *
import random
point_dict = {"01":(135,215),"03":(215,215),"05":(295,215),"07":(375,215),
               "10":(95,255),"11":(135,255),"12":(175,255),"13":(215,255),"14":(255,255),"15":(295,255),"16":(335,255),"17":(375,255),"18":(415,255),
               "21":(135,295),"23":(215,295),"25":(295,295),"27":(375,295),"30":(95,335),"31":(135,335),"32":(175,335),"33":(215,335),"34":(255,335),"35":(295,335),"36":(335,335),"37":(375,335),"38":(415,335),
               "41":(135,375),"43":(215,375),"45":(295,375),"47":(375,375),
               "50":(95,415),"51":(135,415),"52":(175,415),"53":(215,415),"54":(255,415),"55":(295,415),"56":(335,415),"57":(375,415),"58":(415,415),
               "61":(135,455),"63":(215,455),"65":(295,455),"67":(375,455),
               "70":(95,495),"71":(135,495),"72":(175,495),"73":(215,495),"74":(255,495),"75":(295,495),"76":(335,495),"77":(375,495),"78":(415,495),
               "81":(135,535),"83":(215,535),"85":(295,535),"87":(375,535)}

def main():
    pygame.init()
    white = (255, 246, 143) 
    screen = pygame.display.set_mode((500,600))
    pygame.display.set_caption('Dot and Box')
    scoreX = 0
    scoreY = 0
    turn = 'A'
    font = pygame.font.Font('freesansbold.ttf', 18)
    
    textA = font.render('player A score: '+str(scoreX), True, (0,0,0))
    textB = font.render('player B score: '+str(scoreY), True, (0,0,0))

    textRectA = textA.get_rect()
    textRectA.center = (100,30)
    textRectB = textB.get_rect()
    textRectB.center = (380,30)
    # load all images
    A = pygame.image.load("pics/A.png")
    B = pygame.image.load("pics/B.png")
    dot = pygame.image.load("pics/dot.png")
    lineX = pygame.image.load("pics/lineX.png")
    lineY = pygame.image.load("pics/lineY.png")
    background = pygame.image.load("pics/background.png")
    dot = pygame.transform.scale(dot, (30, 30))
    lineX = pygame.transform.scale( lineX, (70, 12))
    lineY = pygame.transform.scale( lineY, (12, 70))
    A = pygame.transform.scale( A, (50, 50))
    backA = pygame.transform.scale( background, (50, 50))
    B = pygame.transform.scale(B, (50, 50))
    backB = pygame.transform.scale(background, (50, 50))

    backTextA = pygame.transform.scale( background, (180, 20))
    backTextB = pygame.transform.scale( background, (180, 20))

    font1 = pygame.font.Font('freesansbold.ttf', 60) 
    AwinText = font1.render('player A wins', True, (0,0,255))
    BwinText = font1.render('player B wins', True, (0,0,255))
    AwinTextRect = AwinText.get_rect()
    AwinTextRect.center = (250,100)
    BwinTextRect = BwinText.get_rect()
    BwinTextRect.center = (250,100)

    font2 = pygame.font.Font('freesansbold.ttf', 20) 
    turnA = font1.render('player A turn', True, (0,0,255))
    turnB = font1.render('player B turn', True, (0,0,255))
    turnARect = turnA.get_rect()
    turnARect.center = (250,100)
    turnBRect = turnB.get_rect()
    turnBRect.center = (250,100)

    backTurn = pygame.transform.scale(background, (500,100))
    
    game = DotsAndBoxes(initial_player=-1,rows=5,cols=5)
    running = True
    show(screen,white,textA,textRectA,textB, textRectB,dot,turnA,turnARect,backTurn)
    level = "s"
    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT : 
                pygame.quit() 
                quit()
                               
            elif game.turn == 1 and level == "s" and game.is_over is not False:
                move = simple_player(game)
                if move is not None:
                    game.play(move = move)
                if game.turn == -1:
                    screen.blit(turnA,turnARect)
                else:
                    screen.blit(turnB,turnBRect)
                scoreX = game.score[0]
                scoreY = game.score[1]
                
                textA = font.render('player A score: '+str(scoreX), True, (0,0,0))
                textB = font.render('player B score: '+str(scoreY), True, (0,0,0))
                screen.blit(textA, textRectA)
                screen.blit(textB, textRectB)

                font.render('player A score: '+str(scoreX), True, white)
                font.render('player B score: '+str(scoreY), True, white)
                update(game.board,screen,A,B,lineX,lineY,backA,backB)
                if game.is_over():
                    if scoreX>scoreY:
                        screen.blit(backTurn, turnARect)
                        screen.blit(AwinText,AwinTextRect)
                    else:
                        screen.blit(backTurn, turnARect)
                        screen.blit(BwinText,BwinTextRect)
                pygame.display.flip()
                
                screen.blit(backTextA, textRectA)
                screen.blit(backTextB, textRectB)
                screen.blit(backTurn, turnARect)
            elif game.turn == 1 and level == "m" and game.is_over is not False:
                move = mid_player(game)
                if move is not None:
                    game.play(move = move)
                if game.turn == -1:
                    screen.blit(turnA,turnARect)
                else:
                    screen.blit(turnB,turnBRect)
                scoreX = game.score[0]
                scoreY = game.score[1]
                
                textA = font.render('player A score: '+str(scoreX), True, (0,0,0))
                textB = font.render('player B score: '+str(scoreY), True, (0,0,0))
                screen.blit(textA, textRectA)
                screen.blit(textB, textRectB)

                font.render('player A score: '+str(scoreX), True, white)
                font.render('player B score: '+str(scoreY), True, white)
                update(game.board,screen,A,B,lineX,lineY,backA,backB)
                if game.is_over():
                    if scoreX>scoreY:
                        screen.blit(backTurn, turnARect)
                        screen.blit(AwinText,AwinTextRect)
                    else:
                        screen.blit(backTurn, turnARect)
                        screen.blit(BwinText,BwinTextRect)
                pygame.display.flip()
                
                screen.blit(backTextA, textRectA)
                screen.blit(backTextB, textRectB)
                screen.blit(backTurn, turnARect)
            elif game.turn == 1 and level == "h" and game.is_over is not False:
                move = high_player(game)
                if move is not None:
                    game.play(move = move)
                if game.turn == -1:
                    screen.blit(turnA,turnARect)
                else:
                    screen.blit(turnB,turnBRect)
                scoreX = game.score[0]
                scoreY = game.score[1]
                
                textA = font.render('player A score: '+str(scoreX), True, (0,0,0))
                textB = font.render('player B score: '+str(scoreY), True, (0,0,0))
                screen.blit(textA, textRectA)
                screen.blit(textB, textRectB)

                font.render('player A score: '+str(scoreX), True, white)
                font.render('player B score: '+str(scoreY), True, white)
                update(game.board,screen,A,B,lineX,lineY,backA,backB)
                if game.is_over():
                    if scoreX>scoreY:
                        screen.blit(backTurn, turnARect)
                        screen.blit(AwinText,AwinTextRect)
                    else:
                        screen.blit(backTurn, turnARect)
                        screen.blit(BwinText,BwinTextRect)
                pygame.display.flip()
                
                screen.blit(backTextA, textRectA)
                screen.blit(backTextB, textRectB)
                screen.blit(backTurn, turnARect)
            elif game.turn == -1 and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                print(x,y)
                
                wall_x,wall_y =  get_wall(x,y)
                key = get_key(point_dict,wall_x,wall_y)

                if not (wall_x >= 0 and wall_y >= 0):
                    continue
                
                if (wall_y-215) % 80 == 0:
                    game.play(i = int(key[0]),j = int(key[1]))
                    screen.blit( lineX, (wall_x-35, wall_y-7))
                    
                else:
                    game.play(i = int(key[0]),j = int(key[1]))
                    screen.blit( lineY, (wall_x-6, wall_y-35))
                if game.turn == -1:
                    screen.blit(turnA,turnARect)
                else:
                    screen.blit(turnB,turnBRect)
                scoreX = game.score[0]
                scoreY = game.score[1]
                
                textA = font.render('player A score: '+str(scoreX), True, (0,0,0))
                textB = font.render('player B score: '+str(scoreY), True, (0,0,0))
                screen.blit(textA, textRectA)
                screen.blit(textB, textRectB)

                font.render('player A score: '+str(scoreX), True, white)
                font.render('player B score: '+str(scoreY), True, white)
                update(game.board,screen,A,B,lineX,lineY,backA,backB)
                if game.is_over():
                    if scoreX>scoreY:
                        screen.blit(backTurn, turnARect)
                        screen.blit(AwinText,AwinTextRect)
                    else:
                        screen.blit(backTurn, turnARect)
                        screen.blit(BwinText,BwinTextRect)
                pygame.display.flip()
                
                screen.blit(backTextA, textRectA)
                screen.blit(backTextB, textRectB)
                screen.blit(backTurn, turnARect)
    

    return        

def show(screen,white,textA,textRectA,textB, textRectB,dot,turnA,turnARect,backTurn):
    """
    Reload the screen
    Use the current grid and wall information to
    update the players screen
    """
    screen.fill( white)
    
    clock = pygame.time.Clock()
    #background music
    pygame.display.update()
    pygame.mixer.music.load('backmusic.mp3')
    pygame.mixer.music.play()
    clock.tick(5)

    # loop over all slots
    for column in range(5):
        for row in range(5):
            x, y = column * 80+80, row * 80+200
            screen.blit(dot, (x, y))
            x += 4
    screen.blit(textA, textRectA)
    screen.blit(textB, textRectB)
    screen.blit(turnA,turnARect)
    pygame.display.flip()
    screen.blit(backTurn, turnARect)
    
def get_wall(x,y):
    rest_x = (x-85)%80
    rest_y = (y-205)%80

    wall_slot_x = x//80
    wall_slot_y = (y-205)//80
    if rest_x<20 and rest_y<20:
        return -1,-1
    if x-85<0 or y-205<0 or x-420>=0 or y-540>=0:
        return -1,-1
    if rest_x<20:
        return wall_slot_x*80+15, wall_slot_y*80+215+40
    if rest_y<20:
        return wall_slot_x*80+40+15, wall_slot_y*80+215
    return -1,-1

def get_key(mydict,x,y):
    for key in mydict.keys():
        if mydict[key]==(x,y):
            return key

def update(board,screen,A,B,lineX,lineY,backA,backB):
    if pygame.mixer.music.get_busy() == False:
        clock = pygame.time.Clock()
        #background music
        pygame.display.update()
        pygame.mixer.music.load('backmusic.mp3')
        pygame.mixer.music.play()
        clock.tick(5)

    for i in range(9):
        for j in range(9):
            if i%2!=0 and j%2!=0:
                if board[i,j] == 1:
                    wall_x,wall_y = point_dict[str(i)+str(j)]
                    screen.blit(backA,(wall_x-25,wall_y-25))
                    screen.blit(B,(wall_x-25,wall_y-25))
                elif board[i,j] == -1:
                    wall_x,wall_y = point_dict[str(i)+str(j)]
                    screen.blit(backB,(wall_x-25,wall_y-25))
                    screen.blit(A,(wall_x-25,wall_y-25))
            elif board[i,j] != 0:
                wall_x,wall_y = point_dict[str(i)+str(j)]
                if (wall_y-215) % 80 == 0:
                    screen.blit(lineX, (wall_x-35, wall_y-7))
                        
                else:
                    screen.blit(lineY, (wall_x-6, wall_y-35))
    return
def simple_player(game):
    move_list = game.getmovelist()
    if len(move_list) == 0:
        return None
    print(move_list)
    print(game.board)
    smallest = 1000
    if game.check_fill_move():
        return game.check_fill_move() 
    for i in range(0,game.r):
        for j in range(0,game.c):
            if i%2!=0 and j%2!=0 and game.board[i,j] == 0: 
                if game.check_two_lines(i,j):
                    a,b = game.check_two_lines(i,j)
                    if a in move_list:
                        move_list.remove(a)
                    if b in move_list:
                        move_list.remove(b) 
    if len(move_list) != 0:
        return random.choice(move_list)
    else:
        move_list = game.getmovelist()
    for move in move_list:
        newgame = DotsAndBoxes(game_obj=game)
        num = cal_filled_all(newgame,move)
        if num < smallest:
                bestmove = move
    return bestmove
def mid_player(game):
    move_list = game.getmovelist()
    if len(move_list) == 0:
        return None
    smallest = 1000
    if game.check_fill_move():
        return game.check_fill_move() 
    for i in range(0,game.r):
        for j in range(0,game.r):
            if i%2!=0 and j%2!=0 and game.board[i,j] == 0:                 
                if game.check_two_lines(i,j):
                    a,b = game.check_two_lines(i,j)
                    if a in move_list:
                        move_list.remove(a)
                    if b in move_list:
                        move_list.remove(b)  
    if len(move_list) != 0:
        return random.choice(move_list)    
    if len(move_list) == 0:
        move_list = game.getmovelist()
    dic = {}
    score, move = aplhabeta(game,dic,-10000,10000,"Max")  
    return move
def high_player(game):
    move_list = game.getmovelist()
    for i in range(0,game.r):
        for j in range(0,game.c):
            if i%2!=0 and j%2!=0 and game.board[i,j] == 0:
                if game.check_two_lines(i,j):
                    a,b = game.check_two_lines(i,j)
                    if a in move_list:
                        move_list.remove(a)
                    if b in move_list:
                        move_list.remove(b) 
    if game.check_fill_move() and move_list is not []:
        return game.check_fill_move()
    lis = game.check_empty_lines()
    if len(lis) != 0:
        return random.choice(lis)
    dic = {}
    return aplhabeta(game,dic,-10000,10000,"Max")[1]
def aplhabeta(game,dic,aplah,beta,minOrMax):
    if game.is_over():
        player_score = game.score[1]
        opponent_score = game.score[0]
        dic[game.board.tobytes()] = player_score - opponent_score
        dic[np.flipud(game.board).tobytes()] = player_score - opponent_score
        dic[np.flip(game.board).tobytes()] = player_score - opponent_score
        dic[np.fliplr(game.board).tobytes()] = player_score - opponent_score
        return player_score - opponent_score, None
    if game.score[1] >= (((game.rows-1)*(game.cols-1))//2 +1):
        dic[game.board.tobytes()] = 1
        dic[np.flipud(game.board).tobytes()] = 1
        dic[np.flip(game.board).tobytes()] = 1
        dic[np.fliplr(game.board).tobytes()] = 1
        return 5, game.getmovelist()[0]
    if game.board.tobytes() in dic:
        return dic[game.board.tobytes()],None
    if minOrMax == "Max":
        v = -1000
        move_list = game.getmovelist()
        best_move, best_score = move_list[0], v
        for move in move_list:
            newgame = DotsAndBoxes(game_obj=game)
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
        best_move, best_score = move_list[0], v
        for move in move_list:
            newgame = DotsAndBoxes(game_obj=game)
            newgame.play(move)
            if newgame.turn == game.turn:
                v = min(v, aplhabeta(newgame,dic,aplah,beta,"Min")[0])
            else:
                v = min(v, aplhabeta(newgame,dic,aplah,beta,"Max")[0])
            if v < best_score:
                best_move = move
                best_score = v
            beta = min(beta, v)
            if beta <= aplah:
                break
        dic[game.board.tobytes()] = v
        dic[np.flipud(game.board).tobytes()] = v
        dic[np.flip(game.board).tobytes()] = v
        dic[np.fliplr(game.board).tobytes()] = v          
        return v, best_move    
        
def minmax(game, player):
    if game.is_over():
        player_score = game.score[1]
        opponent_score = game.score[0]
        print("base")
        return player_score - opponent_score,None
    move_list = game.getmovelist()
    print(move_list)
    minscore = 1000
    maxscore = -1000
    if game.turn == 1:
        for move in move_list:
            newgame = DotsAndBoxes(game_obj=game)
            newgame.play(move)
            score,thisMove = minmax(newgame,newgame.turn)
            if score > maxscore:
                maxscore = score
                bestmove = move
        return maxscore,bestmove
    if game.turn == -1:
        for move in move_list:
            newgame = DotsAndBoxes(game_obj=game)
            newgame.play(move)
            score,thisMove = minmax(newgame,newgame.turn)
            if score < minscore:
                minscore = score
                bestmove = move
        return minscore,bestmove    

            
    
    



def cal_filled_all(game,move):
    gameon = DotsAndBoxes(game_obj=game)
    filledNum = 1 
    gameon.play(move = move)
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

main()
