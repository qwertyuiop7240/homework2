from tkinter import *
import random

root = Tk()
game_run = True
field = []
cross_count = 0
end_game = False
end_comb = []


def who_first_play(value):
    global first_play
    if value:
        first_play = 1
    else:
        first_play = 0


def start_window(window):
    window.title("Игра 'Крестики нолики'")
    i_first = Button(window, text='Я хочу начать первым',
                     command=lambda: [who_first_play(1), change_window_start_on_window_game(), new_game()])
    i_no_first = Button(window, text='Пусть компьютер начнет первым',
                        command=lambda: [who_first_play(0), change_window_start_on_window_game(), new_game()])
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
                            command=lambda row=row, col=col: [click(row, col), check_win(field)])
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)
    window_center(window)
    window.mainloop()


def window_center(window):
    window.update_idletasks()
    w, h = window.winfo_width(), window.winfo_height()
    window.geometry(f'+{(window.winfo_screenwidth() - w) // 2}+{(window.winfo_screenheight() - h) // 2}')


def change_window_start_on_window_game():
    global window_game
    window_game = Toplevel()
    game_window(window_game)


def question_about_continuation():
    window_question = Toplevel()
    button_question_yes = Button(window_question, text='Да',
                                 command=lambda: [window_question.destroy(), new_game()])
    button_question_no = Button(window_question, text='Нет',
                                command=lambda: [window_question.destroy(), window_game.destroy(), root.destroy()])
    Label(window_question, text='Ещё?)').grid(row=0, column=2, sticky=N + S + W + E, padx=5,
                                              pady=5, ipadx=5,
                                              ipady=5)
    button_question_yes.grid(row=1, column=1, sticky=N + S + W + E, padx=5, pady=5, ipadx=5, ipady=5)
    button_question_no.grid(row=1, column=3, columnspan=2, sticky=N + S + W + E, padx=5, pady=5, ipadx=5, ipady=5)
    window_center(window_question)


def new_game():
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
            field[row][col]['fg'] = 'black'
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


def check_win(field):
    def check_win_horizontal(field):
        win_check = False
        finish_comb = []
        for row in range(10):
            for col in range(6):
                if field[row][col]['text'] == 'X':
                    if all((
                            field[row][col + 1]['text'] == 'X',
                            field[row][col + 2]['text'] == 'X',
                            field[row][col + 3]['text'] == 'X',
                            field[row][col + 4]['text'] == 'X'
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row, col + i])
                        finish_comb.append(win_check)
                        return finish_comb
                if field[row][col]['text'] == 'O':
                    if all((
                            field[row][col + 1]['text'] == 'O',
                            field[row][col + 2]['text'] == 'O',
                            field[row][col + 3]['text'] == 'O',
                            field[row][col + 4]['text'] == 'O'
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row, col + i])
                        finish_comb.append(win_check)
                        return finish_comb
        return win_check

    def check_win_vertical(field):
        win_check = False
        finish_comb = []
        for col in range(10):
            for row in range(6):
                if field[row][col]['text'] == 'X':
                    if all((
                            field[row + 1][col]['text'] == 'X',
                            field[row + 2][col]['text'] == 'X',
                            field[row + 3][col]['text'] == 'X',
                            field[row + 4][col]['text'] == 'X'
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row + i, col])
                        finish_comb.append(win_check)
                        return finish_comb
                if field[row][col]['text'] == 'O':
                    if all((
                            field[row + 1][col]['text'] == 'O',
                            field[row + 2][col]['text'] == 'O',
                            field[row + 3][col]['text'] == 'O',
                            field[row + 4][col]['text'] == 'O'
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row + i, col])
                        finish_comb.append(win_check)
                        return finish_comb
        return win_check

    def check_win_diagonal_right(field):
        win_check = False
        finish_comb = []
        for row in range(6):
            for col in range(6):
                if field[row][col]['text'] == 'X':
                    if all((
                            field[row + 1][col + 1]['text'] == 'X',
                            field[row + 2][col + 2]['text'] == 'X',
                            field[row + 3][col + 3]['text'] == 'X',
                            field[row + 4][col + 4]['text'] == 'X'
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row + i, col + i])
                        finish_comb.append(win_check)
                        return finish_comb
                if field[row][col]['text'] == 'O':
                    if all((
                            field[row + 1][col + 1]['text'] == 'O',
                            field[row + 2][col + 2]['text'] == 'O',
                            field[row + 3][col + 3]['text'] == 'O',
                            field[row + 4][col + 4]['text'] == 'O'
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row + i, col + i])
                        finish_comb.append(win_check)
                        return finish_comb
        return win_check

    def check_win_diagonal_left(field):
        win_check = False
        finish_comb = []
        for row in range(6):
            for col in range(9, 3, -1):
                if field[row][col]['text'] == 'X':
                    if all((
                            field[row + 1][col - 1]['text'] == 'X',
                            field[row + 2][col - 2]['text'] == 'X',
                            field[row + 3][col - 3]['text'] == 'X',
                            field[row + 4][col - 4]['text'] == 'X'
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row + i, col - i])
                        finish_comb.append(win_check)
                        return finish_comb
                if field[row][col]['text'] == 'O':
                    if all((
                            field[row + 1][col - 1]['text'] == 'O',
                            field[row + 2][col - 2]['text'] == 'O',
                            field[row + 3][col - 3]['text'] == 'O',
                            field[row + 4][col - 4]['text'] == 'O'
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row + i, col - i])
                        finish_comb.append(win_check)
                        return finish_comb
        return win_check

    def display_win(field):
        if end_game:
            for i in range(5):
                row = end_comb[i][0]
                col = end_comb[i][1]
                if first_play == 1 and field[row][col]['text'] == 'X':
                    field[row][col]['fg'] = 'green'
                elif first_play == 0 and field[row][col]['text'] == 'O':
                    field[row][col]['fg'] = 'green'
                else:
                    field[row][col]['fg'] = 'red'

    global end_comb
    global end_game
    if (end_comb := check_win_diagonal_right(field)) != False:
        end_game = end_comb[-1]
        display_win(field)
        question_about_continuation()
        print(end_comb)
    elif (end_comb := check_win_diagonal_left(field)) != False:
        end_game = end_comb[-1]
        display_win(field)
        question_about_continuation()
        print(end_comb)
    elif (end_comb := check_win_horizontal(field)) != False:
        end_game = end_comb[-1]
        display_win(field)
        question_about_continuation()
        print(end_comb)
    elif (end_comb := check_win_vertical(field)) != False:
        end_game = end_comb[-1]
        display_win(field)
        question_about_continuation()
        print(end_comb)
    else:
        end_game = False
        print(end_game)


start_window(root)
