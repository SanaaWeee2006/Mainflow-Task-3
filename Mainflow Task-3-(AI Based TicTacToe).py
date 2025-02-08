# ---AI BASED TIC TAC TOE---

import math

board = [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    elif winner == "O":
        return 10 - depth
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move

def player_move():
    while True:
        try:
            row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column between 0 and 2.")

def play_game():
    print("Tic-Tac-Toe: You (X) vs AI (O)")
    print_board(board)

    for turn in range(9):  
        if turn % 2 == 0:  # Player's turn
            player_move()
        else:  # AI's turn
            row, col = best_move(board)
            board[row][col] = "O"
            print("AI's Move:")
        
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Winner: {winner} 🎉")
            return

    print("It's a tie! 🤝")

play_game()
