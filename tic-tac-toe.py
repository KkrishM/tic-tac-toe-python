import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def player_move():
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if 0 <= move <= 8 and board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Invalid move, try again!")

def computer_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"
    print(f"Computer chose position {move + 1}")

def play_game():
    print("🎮 Welcome to Tic Tac Toe!")
    print("You are X and Computer is O")

    while True:
        print_board()
        player_move()

        if check_winner("X"):
            print_board()
            print("🎉 You win!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a draw!")
            break

        computer_move()

        if check_winner("O"):
            print_board()
            print("💻 Computer wins!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a draw!")
            break

play_game()
