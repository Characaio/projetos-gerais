import random

possible_play = ['rock', 'paper', 'scissors']
past_plays = []
def new_game():
    past_plays.clear()
    play = input(str('chosse a move:'))
    while play not in possible_play:
        play = input('chosse a move:')
    random.shuffle(possible_play)
    enemy_play = possible_play[1]
    if play == 'rock' and enemy_play == 'scissors':
        print('player wins')
    elif play == 'rock' and enemy_play == 'paper':
        print('player loses')
    elif play == 'rock' and enemy_play == 'rock':
        print('tie')
    elif play == 'paper' and enemy_play == 'scissors':
        print('player loses')
    elif play == 'paper' and enemy_play == 'paper':
        print('tie')
    elif play == 'paper' and enemy_play == 'rock':
        print('player wins')
    elif play == 'scissors' and enemy_play == 'scissors':
        print('tie')
    elif play == 'scissors' and enemy_play == 'paper':
        print('player wins')
    elif play == 'scissors' and enemy_play == 'rock':
        print('player loses')
    repeat.lower() = input('play again?: Y/N')
    if repeat == 'Y':
        new_game()
    else:
        print('fuck you')
        exit()
        quit()
new_game()
    
