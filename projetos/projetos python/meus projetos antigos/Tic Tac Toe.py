import tkinter as tk
import random
from random import choice

root = tk.Tk()

root.geometry('300x300')
root.title('Tic Tac Toe')
players = ['X', 'O']
winner = False
wins_by_X = 0
wins_by_O = 0
possible_coords = [0,1,2]
its_done = False
mode = 'AI'

def new_game(label, buttons1): # limpa o jogo anterior
    global clear
    global winner
    winner = False
    clear = True

    global player
    player = players[0]


    label2.config(text='')
    print(player)
    for row in range(3):
        for column in range(3):
            buttons1[row][column]['text'] = ''

who_win_is = ''
def winner_is_X(): # sinaliza que o vencedor é X
    label2.config(text='o jogador ' + players[0] + ' ganhou o jogo')
    global winner
    winner = True
    who_win_is = players[0]
    global wins_by_X
    wins_by_X += 1

def winner_is_O(): #sinaliza que o vencedor é O
    label2.config(text='o jogador ' + players[1] + ' ganhou o jogo')
    global winner
    winner = True
    who_win_is = players[1]
    global wins_by_O
    wins_by_O += 1

def check_for_o_win(): #isso checa se o jogador O ganhou o jogo
    # checa as possibilidades de vitoria e retorna se é verdadeiro(vitoria) ou não(falso)
    if buttons[0][0]['text'] == players[1] and buttons[0][1]['text'] == players[1] and buttons[0][2]['text'] == players[1]:
        return True
    elif buttons[0][0]['text'] == players[1] and buttons[1][0]['text'] == players[1] and buttons[2][0]['text'] == players[1]:
        return True
    elif buttons[0][0]['text'] == players[1] and buttons[1][1]['text'] == players[1] and buttons[2][2]['text'] == players[1]:
        return True
    elif buttons[0][2]['text'] == players[1] and buttons[1][1]['text'] == players[1] and buttons[2][0]['text'] == players[1]:
        return True
    elif buttons[2][0]['text'] == players[1] and buttons[2][1]['text'] == players[1] and buttons[2][2]['text'] == players[1]:
        return True
    elif buttons[0][2]['text'] == players[1] and buttons[1][2]['text'] == players[1] and buttons[2][2]['text'] == players[1]:
        return True
    elif buttons[0][1]['text'] == players[1] and buttons[1][1]['text'] == players[1] and buttons[2][1]['text'] == players[1]:
        return True
    elif buttons[1][0]['text'] == players[1] and buttons[1][1]['text'] == players[1] and buttons[1][2]['text'] == players[1]:
        return True
    else:
        return False

def check_for_x_win(): #isso checa se o jogador X ganhou o jogo
    #checa as possibilidades de vitoria e retorna se é verdadeiro(vitoria) ou não(falso)
    if buttons[0][0]['text'] == players[0] and buttons[0][1]['text'] == players[0] and buttons[0][2]['text'] == players[0]:
        return True
    elif buttons[0][0]['text'] == players[0] and buttons[1][0]['text'] == players[0] and buttons[2][0]['text'] == players[0]:
        return True
    elif buttons[0][0]['text'] == players[0] and buttons[1][1]['text'] == players[0] and buttons[2][2]['text'] == players[0]:
        return True
    elif buttons[0][2]['text'] == players[0] and buttons[1][1]['text'] == players[0] and buttons[2][0]['text'] == players[0]:
        return True
    elif buttons[2][0]['text'] == players[0] and buttons[2][1]['text'] == players[0] and buttons[2][2]['text'] == players[0]:
        return True
    elif buttons[0][2]['text'] == players[0] and buttons[1][2]['text'] == players[0] and buttons[2][2]['text'] == players[0]:
        return True
    elif buttons[0][1]['text'] == players[0] and buttons[1][1]['text'] == players[0] and buttons[2][1]['text'] == players[0]:
        return True
    elif buttons[1][0]['text'] == players[0] and buttons[1][1]['text'] == players[0] and buttons[1][2]['text'] == players[0]:
        return True
    else:
        return False

def check_for_tie(): #checa se o resultado é um empate
    global buttons
    #checa se todos os botôes estão com algum caractere atribuido
    if (buttons[0][0]['text'] != '' and buttons[0][1]['text'] != '' and
        buttons[0][2]['text'] != '' and buttons[1][0]['text'] != '' and
        buttons[1][1]['text'] != '' and buttons[1][2]['text'] != '' and
        buttons[2][0]['text'] != '' and buttons[2][1]['text'] != '' and
        buttons[2][2]['text'] != ''):
        if check_for_x_win() is True or check_for_o_win(): #checa se o X ou O ganhou no ultimo turno
            return False
        else:
            return True
    else:
        return False

def winner_is_tie():
    label2.config(text='isso é um empate')
    global winner
    winner = 'Tie'
    who_win_is = 'tie'
    return 'tie'

def get_player_mode(type):
    global mode
    mode = type
    global label1
    global buttons
    new_game(label1, buttons)


def circle_simple_ai():
    global its_done
    its_done = False
    global who_wins_is
    global winner
    if check_for_tie() is False: #checa para ver se é um mepate
        if check_for_x_win() is False: #checa se o 'X' venceu para previnir substituição de caractere e vitoria/empate falso
            while its_done == False: #checa varias alternativas para achar uma aleatoria que da certo
                global rowI
                global columnI
                rowI = random.choice(possible_coords) # linha aleatoria
                columnI = random.choice(possible_coords) #coluna aleatoria
                if buttons[rowI][columnI]['text'] == '':
                    its_done = True
                    break
                else:
                    if winner == False:
                        continue
                    elif winner == True:
                        break
            return True
        else:
            pass
    else:
        winner_is_tie()

def next_turn(row, column):
    print(winner)
    global player
    if player == players[0] and buttons[row][column]['text'] == '':
        if winner == False:
            buttons[row][column]['text'] = players[0]
            its_done = False
        player = players[1]
        print(player + 'next turn')
        # checa se o jogador 'X' ganhou
        if check_for_x_win() is True:
            winner_is_X()
        else:
            if check_for_tie() is True:

                winner_is_tie()
            else:
                player = players[1]

    global mode
    if player == players[1] and mode == 'AI': #isso começa o turno do jogador 'O'
        its_done = False
        #isso espera o retorno da função para permitir que a IA do jogador 'O' consiga jogar em um espaço valido
        if circle_simple_ai() is True:
            print('this tile is not occupied')
            global rowI
            global columnI
            buttons[rowI][columnI]['text'] = players[1]
            #checa se o jogador 'O' ganhou
            if check_for_o_win() is True:
                winner_is_O()
            else:
                if check_for_tie() is True:
                    winner_is_tie()
                else:
                    player = players[0]

    elif player == players[1] and mode == 'Player':
        print(winner)
        if player == players[1] and buttons[row][column]['text'] == '':
            if winner == False:
                buttons[row][column]['text'] = players[1]
                its_done = False
            player = players[0]
            print(player + 'next turn')
            # checa se o jogador 'X' ganhou
            if check_for_o_win() is True:
                winner_is_O()
            else:
                if check_for_tie() is True:
                    winner_is_tie()
                else:
                    player = players[0]






frame = tk.Frame(root)
frame.pack()

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
global clear

for row in range(3):
    for column in range(3):
        buttons[row][column] = tk.Button(frame, text='', width=5, height=2,
                                        command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

    clear = False
frame2 = tk.Frame(root)
frame2.pack()
label1 = tk.Label(root, text='')
label2 = tk.Label(root, text='', font=('arial', 14))
restart_btn = tk.Button(frame2, text='new game', command=lambda:new_game(label1, buttons))
AI_mode = tk.Button(frame2, text=players[1]+ ' é IA',command=lambda: get_player_mode('AI'))
Player_mode = tk.Button(frame2, text=players[1] + ' é jogador',command=lambda: get_player_mode('Player'))
new_game(label1, buttons)


label1.pack(side='top')
restart_btn.grid(row=0, column=0, pady=2)
AI_mode.grid(row=1, column=0, pady=2)
Player_mode.grid(row=2, column=0, pady=2)
label2.pack()



root.mainloop()
