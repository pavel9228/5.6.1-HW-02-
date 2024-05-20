board = list(range(1, 10))
end = False
win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def game_board():
    print(board[0], board[1], board[2], sep=" | ")
    print(board[3], board[4], board[5], sep=" | ")
    print(board[6], board[7], board[8], sep=" | ")

def player1 ():  #Функция 1 игрока (крестик)
    n = enter_numb()  #Выбор клетки
    if board[n] == "X" or board[n] == "O":
        print("Клетка занята! Попробуйте еще раз!")
        player1()
    else:
        board[n] = "X"

def player2 ():  #Функция 2 игрока (нолик)
    n = enter_numb()  #Выбор клетки
    if board[n] == "X" or board[n] == "O":
        print("Клетка занята! Попробуйте еще раз!")
        player2()
    else:
        board[n] = "O"

def enter_numb():  #Функция ввода данных
    while True:
        while True:
            a = input()
            try:
                a = int(a)
                a -= 1
                if a in range(0, 9):
                    return a
                else:
                    print("Не правильный ввод! Попробуйте еще раз!")
                    continue
            except ValueError:
                    print("\nThat's not a number. Try again")
                    continue

def win_board():  #Функция опеределения победителя
    count = 0  #Счетчик ходов
    for a in win_commbinations:
        if board[a[0]] == board[a[1]] == board[a[2]] == "X":
            print("Крестики победили")
            return True
        if board[a[0]] == board[a[1]] == board[a[2]] == "O":
            print("Нолики победили")
            return True
    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            count += 1
        if count == 9:
            print("Ничья!")
            return True
while not end:
        game_board()
        end = win_board()
        if end == True:
            break
        print("Ходят крестики:")
        player1()
        print()
        game_board()
        end = win_board()
        if end == True:
            break
        print("Ходят нолики:")
        player2()
        print()
