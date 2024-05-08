
board = [' ' for _ in range(9)]


def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def check_winner(player):
    
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True


    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True


    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False


def make_move(player):
    while True:
        move = input(f"Игрок {player}, введите номер ячейки (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)-1] == ' ':
            board[int(move)-1] = player
            break
        else:
            print("Некорректный ход, попробуйте еще раз.")


def play_game():
    print_board()
    current_player = 'X'
    while True:
        make_move(current_player)
        print_board()
        if check_winner(current_player):
            print(f"Игрок {current_player} победил!")
            break
        if ' ' not in board:
            print("Ничья!")
            break
        current_player = 'O' if current_player == 'X' else 'X'


play_game()
