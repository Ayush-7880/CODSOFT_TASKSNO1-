# CODSOFT AI Internship - Task 2
# Tic-Tac-Toe AI
# Human vs AI using Minimax Algorithm

import math


def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c]:
            return board[a]

    if all(position in ["X", "O"] for position in board):
        return "Draw"

    return None


def minimax(board, depth, is_maximizing):
    result = check_winner(board)

    if result == "O":
        return 10 - depth

    if result == "X":
        return depth - 10

    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] not in ["X", "O"]:
                board[i] = "O"

                score = minimax(
                    board,
                    depth + 1,
                    False
                )

                board[i] = str(i + 1)
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] not in ["X", "O"]:
                board[i] = "X"

                score = minimax(
                    board,
                    depth + 1,
                    True
                )

                board[i] = str(i + 1)
                best_score = min(best_score, score)

        return best_score


def find_best_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] not in ["X", "O"]:
            board[i] = "O"

            score = minimax(
                board,
                0,
                False
            )

            board[i] = str(i + 1)

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def main():
    board = [str(i) for i in range(1, 10)]

    print("=" * 35)
    print("       TIC-TAC-TOE AI")
    print("=" * 35)

    print("\nYou are X")
    print("AI is O")
    print("Choose a position from 1 to 9.")

    print_board(board)

    while True:

        # Human move
        while True:
            try:
                move = int(
                    input("Enter your move (1-9): ")
                )

                if move < 1 or move > 9:
                    print(
                        "Please enter a number "
                        "between 1 and 9."
                    )
                    continue

                index = move - 1

                if board[index] in ["X", "O"]:
                    print(
                        "That position is already occupied."
                    )
                    continue

                board[index] = "X"
                break

            except ValueError:
                print("Please enter a valid number.")

        print_board(board)

        result = check_winner(board)

        if result:
            break

        # AI move
        print("AI is thinking...")

        ai_move = find_best_move(board)
        board[ai_move] = "O"

        print(
            f"AI chose position {ai_move + 1}."
        )

        print_board(board)

        result = check_winner(board)

        if result:
            break

    # Game result
    if result == "X":
        print("Congratulations! You won!")

    elif result == "O":
        print("AI wins! Better luck next time.")

    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
