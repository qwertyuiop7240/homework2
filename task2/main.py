from tkinter import *
import random

root = Tk()
game_run = True
field = []
cross_count = 0


def who_first_play(value):
    global first_play
    if value:
        first_play = 1
    else:
        first_play = 0


def start_window(window):
    window.title("Игра 'Крестики нолики'")
    i_first = Button(window, text='Я хочу начать первым',
                     command=lambda: [who_first_play(1), change_window_start_on_window_game(window), new_game()])
    i_no_first = Button(window, text='Пусть компьютер начнет первым',
                        command=lambda: [who_first_play(0), change_window_start_on_window_game(window), new_game()])
    i_first.grid(row=0, column=1, columnspan=2, sticky=N + S + W + E, padx=5, pady=5, ipadx=5, ipady=5)
    i_no_first.grid(row=0, column=7, columnspan=2, sticky=N + S + W + E, padx=5, pady=5, ipadx=5, ipady=5)
    window_center(window)
    window.mainloop()


def game_window(window):
    window.title("Игра 'Крестики нолики'")
    for row in range(10):
        line = []
        for col in range(10):
            button = Button(window, text=' ', width=2, height=1,
                            font=('Verdana', 20, 'bold'),
                            background='lavender',
                            command=lambda row=row, col=col: click(row, col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)
    window_center(window)
    window.mainloop()


def window_center(window):
    window.update_idletasks()
    w, h = window.winfo_width(), window.winfo_height()
    window.geometry(f'+{(window.winfo_screenwidth() - w) // 2}+{(window.winfo_screenheight() - h) // 2}')


def change_window_start_on_window_game(window):
    window.destroy()
    window_open = Tk()
    game_window(window_open)


def change_window_game_on_window_start(window):
    window.destroy()
    window_open = Tk()
    start_window(window_open)


def new_game():
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        if first_play:
            field[row][col]['text'] = 'X'
            value = 'O'
        else:
            field[row][col]['text'] = 'O'
            value = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move(value)
            check_win('O')


def check_win(smb):
    for n in range(5):
        check_line(field[n][1], field[n][2], field[n][3], smb)
        check_line(field[1][n], field[2][n], field[3][n], smb)
    check_line(field[1][0], field[1][2], field[2][3], smb)
    check_line(field[3][0], field[1][2], field[0][2], smb)


def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False


def can_win(a1, a2, a3, smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res


def computer_move(value):
    for n in range(5):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(5):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 5)
        col = random.randint(0, 5)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = value
            break


start_window(root)
