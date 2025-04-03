import tkinter as tk

board= [[1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1]]

pieces = [['Tb','Cb','Bb','Qb','Rb','Bb','Cb','Rb'],
          ['Pb','Pb','Pb','Pb','Pb','Pb','Pb','Pb'],
          ['','','','','','','',''],
          ['','','','','','','',''],
          ['','','','','','','',''],
          ['','','','','','','',''],
          ['Pw','Pw','Pw','Pw','Pw','Pw','Pw','Pw'],
          ['Tw','Cw','Bw','Qw','Rw','Bw','Cw','Rw']]

hotbar = ''
class ChessPieces:
    def __init__(self, type, color, location_x, location_y, first_move):
        self.type = type
        self.color = color
        self.location_x = location_x
        self.location_y = location_y
        self.first_move = first_move
    def legal_moves(self, row, column):
        global hotbar
        board[row][column]['text'] = ''
        hotbar = self.type + self.color
        print(hotbar)
        if self.type == 'P':
            pass


def legal_moves(piece):
    print('legal moves')

def define_held_piece(fullname,piece, color, column, row, move):
    pieces[row][column] = ''
    fullname = ChessPieces(piece, color, column, row, move)
    print(fullname.type + '|' + fullname.color + '|' + str(fullname.location_x) + 'column' + '|' + str(
        fullname.location_y) + 'row' + '|' + str(fullname.first_move))
    fullname.legal_moves(row, column)

def move_piece(row, column):
    print(row)
    print(column)
    global hotbar
    global fullname
    if hotbar == '':
        if 'P' in pieces[row][column] :
            legal_moves('P')
            if 'w' in pieces[row][column]:
                define_held_piece('Peão', 'P' , 'w', column, row, True)
            elif 'b' in pieces[row][column]:
                define_held_piece('Peão', 'P', 'b', column, row, True)

        elif 'T' in pieces[row][column]:
            if 'w' in pieces[row][column]:
                define_held_piece('Torre', 'T' , 'w', column, row, False)
            elif 'b' in pieces[row][column]:
                define_held_piece('Torre', 'T', 'b', column, row, False)

        elif 'C' in pieces[row][column]:
            if 'w' in pieces[row][column]:
                define_held_piece('Cavalo', 'C', 'w', column, row, False)
            elif 'b' in pieces[row][column]:
                define_held_piece('Cavalo', 'C', 'b', column, row, False)

        elif 'B' in pieces[row][column]:
            if 'w' in pieces[row][column]:
                define_held_piece('Bispo', 'B', 'w', column, row, False)
            elif 'b' in pieces[row][column]:
                define_held_piece('Bispo', 'B', 'b', column, row, False)

        elif 'Q' in pieces[row][column]:
            if 'w' in pieces[row][column]:
                define_held_piece('Rainha', 'Q', 'w', column, row, False)
            elif 'b' in pieces[row][column]:
                define_held_piece('Rainha', 'Q', 'b', column, row, False)

        elif 'R' in pieces[row][column]:
            if 'w' in pieces[row][column]:
                define_held_piece('Rei', 'R', 'w', column, row, False)
            elif 'b' in pieces[row][column]:
                define_held_piece('Rei', 'R', 'b', column, row, False)
        else:
            pass
    else:
        print('tour piece at hand is' + hotbar)

        pieces[row][column] = hotbar
        board[row][column]['text'] = hotbar

        hotbar = ''

root = tk.Tk()

root.geometry('600x600')
def new_game():
    for row in range(8):
        for column in range(8):
            if board[row][column] == 1:
                board[row][column] = tk.Button(root, text=pieces[row][column], bg='black', fg='white',
                                               height=3, width=6,
                                               command=lambda row=row, column=column: move_piece(int(row), int(column)))
            else:
                board[row][column] = tk.Button(root, text=pieces[row][column], bg='white', fg='black',
                                               height=3, width=6,
                                               command=lambda row=row, column=column: move_piece(row, column))

            board[row][column].grid(row=row, column=column)

btn_restart = tk.Button(root, text='reset board', command= new_game)
btn_restart.grid(row=10, column=0, fil)
new_game()


root.mainloop()