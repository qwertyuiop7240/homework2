from tkinter import *
import random


def map_creation():
    map_i = []
    for row in range(10):
        row_i = []
        for col in range(10):
            row_i.append(0)
        map_i.append(row_i)
    return map_i


person_play = 0
computer_play = 0
root = Tk()
game_run = True
field = []
cross_count = 0
end_game = False
end_comb = []
weight_charts = map_creation()
max_weight = 0
list_of_movies = []
next_move = [5, 5]


def who_first_play(value):
    global person_play
    global computer_play
    if value:
        person_play = 1
        computer_play = 0
    else:
        person_play = 0
        computer_play = 1


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
                            command=lambda row=row, col=col: [click(row, col), check_win(field), play_AI()])
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
    global weight_charts
    weight_charts = map_creation()


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        if person_play:
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
                if person_play == 1 and field[row][col]['text'] == 'X':
                    field[row][col]['fg'] = 'green'
                elif person_play == 0 and field[row][col]['text'] == 'O':
                    field[row][col]['fg'] = 'green'
                else:
                    field[row][col]['fg'] = 'red'

    global end_comb
    global end_game
    if (end_comb := check_win_diagonal_right(field)) != False:
        end_game = end_comb[-1]
        display_win(field)
        question_about_continuation()
    elif (end_comb := check_win_diagonal_left(field)) != False:
        end_game = end_comb[-1]
        display_win(field)
        question_about_continuation()
    elif (end_comb := check_win_horizontal(field)) != False:
        end_game = end_comb[-1]
        display_win(field)
        question_about_continuation()
    elif (end_comb := check_win_vertical(field)) != False:
        end_game = end_comb[-1]
        display_win(field)
        question_about_continuation()
    else:
        end_game = False


def heaviest_weight():
    global weight_charts
    global max_weight
    max_weight = 0
    for row in range(10):
        for col in range(10):
            if weight_charts[row][col] > max_weight:
                max_weight = weight_charts[row][col]


def choice_of_possible_move(field):
    global weight_charts
    global list_of_movies
    global max_weight
    global next_move
    global person_play
    list_of_movies = []
    for row in range(10):
        for col in range(10):
            if weight_charts[row][col] == max_weight:
                list_of_movies.append([row, col])
    random_index = random.randint(0, len(list_of_movies) - 1)
    next_move = list_of_movies[random_index]
    if person_play:
        field[next_move[0]][next_move[1]]['text'] = 'O'
    else:
        field[next_move[0]][next_move[1]]['text'] = 'X'


def first_selection():
    global weight_charts
    for row in range(10):
        for col in range(10):
            if weight_charts[row][col] == -1:
                for i in range(-1, 2):
                    for k in range(-1, 2):
                        try:
                            if weight_charts[row + i][col + k] == 0 and row + i >= 0 and col + k >= 0:
                                weight_charts[row + i][col + k] = 1
                        except IndexError:
                            continue


def second_selection():
    global weight_charts
    global computer_play
    global field
    if computer_play:
        x = 'X'
    else:
        x = 'O'
    for row in range(10):
        for col in range(10):
            if weight_charts[row][col] == 1:
                for i in range(-1, 2):
                    for k in range(-1, 2):
                        try:
                            if (weight_charts[row + i][col + k] == -1) and (row + i >= 0) and (col + k >= 0) and (
                                    field[row + i][col + k]['text'] == x):
                                weight_charts[row][col] = 2
                        except IndexError:
                            continue


def third_selection():
    global weight_charts
    global computer_play
    global field
    if computer_play:
        x = 'X'
    else:
        x = 'O'

    def check_three_horizontal(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-2, -1, 1, 2]:
            try:
                if field[row][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 2:
            three_check = True
        return three_check

    def check_three_vertical(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-2, -1, 1, 2]:
            try:
                if field[row + i][col]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 2:
            three_check = True
        return three_check

    def check_three_diagonal_right(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-2, -1, 1, 2]:
            try:
                if field[row + i][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 2:
            three_check = True
        return three_check

    def check_three_diagonal_left(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-2, -1, 1, 2]:
            try:
                if field[row - i][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 2:
            three_check = True
        return three_check

    for row in range(10):
        for col in range(10):
            if weight_charts[row][col] == 2:
                if (check_three_horizontal(row, col, x)) or (check_three_vertical(row, col, x)) or (
                        check_three_diagonal_right(row, col, x)) or (check_three_diagonal_left(row, col, x)):
                    weight_charts[row][col] = 3


def fourth_selection():
    global weight_charts
    global computer_play
    global field
    if computer_play:
        x = 'X'
    else:
        x = 'O'

    def check_three_horizontal(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-3, -2, -1, 1, 2, 3]:
            try:
                if field[row][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 3:
            three_check = True
        return three_check

    def check_three_vertical(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-3, -2, -1, 1, 2, 3]:
            try:
                if field[row + i][col]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 3:
            three_check = True
        return three_check

    def check_three_diagonal_right(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-3, -2, -1, 1, 2, 3]:
            try:
                if field[row + i][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 3:
            three_check = True
        return three_check

    def check_three_diagonal_left(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-3, -2, -1, 1, 2, 3]:
            try:
                if field[row - i][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 3:
            three_check = True
        return three_check

    for row in range(10):
        for col in range(10):
            if weight_charts[row][col] == 3:
                if (check_three_horizontal(row, col, x)) or (check_three_vertical(row, col, x)) or (
                        check_three_diagonal_right(row, col, x)) or (check_three_diagonal_left(row, col, x)):
                    weight_charts[row][col] = 4


def fifth_selection():
    global weight_charts
    global computer_play
    global field
    if computer_play:
        x = 'X'
    else:
        x = 'O'

    def check_three_horizontal(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-4, -3, -2, -1, 1, 2, 3, 4]:
            try:
                if field[row][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 4:
            three_check = True
        return three_check

    def check_three_vertical(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-4, -3, -2, -1, 1, 2, 3, 4]:
            try:
                if field[row + i][col]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 4:
            three_check = True
        return three_check

    def check_three_diagonal_right(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-4, -3, -2, -1, 1, 2, 3, 4]:
            try:
                if field[row + i][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 4:
            three_check = True
        return three_check

    def check_three_diagonal_left(row, col, x):
        global weight_charts
        three_check = False
        kol = 0
        for i in [-4, -3, -2, -1, 1, 2, 3, 4]:
            try:
                if field[row - i][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 4:
            three_check = True
        return three_check

    for row in range(10):
        for col in range(10):
            if weight_charts[row][col] == 4:
                if (check_three_horizontal(row, col, x)) or (check_three_vertical(row, col, x)) or (
                        check_three_diagonal_right(row, col, x)) or (check_three_diagonal_left(row, col, x)):
                    weight_charts[row][col] = 5


def sixth_selection():
    global weight_charts
    global computer_play
    global field
    if computer_play:
        x = 'O'
    else:
        x = 'X'

    def check_three_horizontal(row, col, x):
        global weight_charts
        kol = 0
        for i in [-2, -1, 1, 2]:
            try:
                if field[row][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 2:
            for i in [-1, 1]:
                try:
                    if field[row][col + i]['text'] == ' ':
                        weight_charts[row][col + i] = 6
                except:
                    continue

    def check_three_vertical(row, col, x):
        global weight_charts
        kol = 0
        for i in [-2, -1, 1, 2]:
            try:
                if field[row + i][col]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 2:
            for i in [-1, 1]:
                try:
                    if field[row + i][col]['text'] == ' ':
                        weight_charts[row + i][col] = 6
                except:
                    continue

    def check_three_diagonal_right(row, col, x):
        global weight_charts
        kol = 0
        for i in [-2, -1, 1, 2]:
            try:
                if field[row + i][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 2:
            for i in [-1, 1]:
                try:
                    if field[row + i][col + i]['text'] == ' ':
                        weight_charts[row + i][col + i] = 6
                except:
                    continue

    def check_three_diagonal_left(row, col, x):
        global weight_charts
        kol = 0
        for i in [-2, -1, 1, 2]:
            try:
                if field[row - i][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 2:
            for i in [-1, 1]:
                try:
                    if field[row - i][col + i]['text'] == ' ':
                        weight_charts[row - i][col + i] = 6
                except:
                    continue

    for row in range(10):
        for col in range(10):
            if weight_charts[row][col] == -1 and field[row][col]['text'] == x:
                check_three_horizontal(row, col, x)
                check_three_vertical(row, col, x)
                check_three_diagonal_right(row, col, x)
                check_three_diagonal_left(row, col, x)


def seventh_selection():
    global weight_charts
    global computer_play
    global field
    if computer_play:
        x = 'O'
    else:
        x = 'X'

    def check_three_horizontal(row, col, x):
        global weight_charts
        kol = 0
        for i in [-3, -2, -1, 1, 2, 3]:
            try:
                if field[row][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 3:
            for i in [-1, 1]:
                try:
                    if field[row][col + i]['text'] == ' ':
                        weight_charts[row][col + i] = 7
                except:
                    continue

    def check_three_vertical(row, col, x):
        global weight_charts
        kol = 0
        for i in [-3, -2, -1, 1, 2, 3]:
            try:
                if field[row + i][col]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 3:
            for i in [-1, 1]:
                try:
                    if field[row + i][col]['text'] == ' ':
                        weight_charts[row + i][col] = 7
                except:
                    continue

    def check_three_diagonal_right(row, col, x):
        global weight_charts
        kol = 0
        for i in [-3, -2, -1, 1, 2, 3]:
            try:
                if field[row + i][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 3:
            for i in [-1, 1]:
                try:
                    if field[row + i][col + i]['text'] == ' ':
                        weight_charts[row + i][col + i] = 7
                except:
                    continue

    def check_three_diagonal_left(row, col, x):
        global weight_charts
        kol = 0
        for i in [-3, -2, -1, 1, 2, 3]:
            try:
                if field[row - i][col + i]['text'] == x:
                    kol += 1
            except:
                continue
        if kol == 3:
            for i in [-1, 1]:
                try:
                    if field[row - i][col + i]['text'] == ' ':
                        weight_charts[row - i][col + i] = 7
                except:
                    continue

    for row in range(10):
        for col in range(10):
            if weight_charts[row][col] == -1 and field[row][col]['text'] == x:
                check_three_horizontal(row, col, x)
                check_three_vertical(row, col, x)
                check_three_diagonal_right(row, col, x)
                check_three_diagonal_left(row, col, x)


def occupied_cells(field):
    global weight_charts
    for row in range(10):
        for col in range(10):
            if field[row][col]['text'] == 'X' or field[row][col]['text'] == 'O':
                weight_charts[row][col] = -1


def play_AI():
    global field
    global weight_charts
    occupied_cells(field)
    first_selection()
    second_selection()
    third_selection()
    fourth_selection()
    fifth_selection()
    sixth_selection()
    seventh_selection()
    heaviest_weight()
    choice_of_possible_move(field)
    check_win(field)
    for i in weight_charts:
        print(i)
    print('-----------------------------')


start_window(root)
