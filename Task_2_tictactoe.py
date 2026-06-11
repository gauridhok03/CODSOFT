import math

player_score = 0
ai_score = 0


def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True

    return False


def is_draw(board):
    return " " not in board


def minimax(board, is_maximizing):

    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score


def ai_move(board):

    best_score = -math.inf
    move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


def player_move(board):

    while True:

        try:
            move = int(input("Enter position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("❌ Invalid position.")
                continue

            if board[move] != " ":
                print("❌ Position already occupied.")
                continue

            board[move] = "X"
            break

        except ValueError:
            print("❌ Please enter a number.")


def show_positions():
    print("""
Board Positions:

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
""")


def play_game(player_name):

    board = [" "] * 9

    while True:

        print_board(board)

        player_move(board)

        if check_winner(board, "X"):
            print_board(board)
            print(f"🎉 {player_name} Wins!")
            return "player"

        if is_draw(board):
            print_board(board)
            print("🤝 Match Draw!")
            return "draw"

        print("\n🤖 AI is thinking...\n")

        ai_move(board)

        if check_winner(board, "O"):
            print_board(board)
            print("🤖 AI Wins!")
            return "ai"

        if is_draw(board):
            print_board(board)
            print("🤝 Match Draw!")
            return "draw"


def main():

    global player_score
    global ai_score

    print("=" * 45)
    print("      NEXUS TIC-TAC-TOE")
    print("      Human (X) vs AI (O)")
    print("=" * 45)

    player_name = input("\nEnter your name: ").title()

    while True:

        print("\n" + "=" * 30)
        print("SCOREBOARD")
        print("=" * 30)
        print(f"{player_name}: {player_score}")
        print(f"AI : {ai_score}")
        print("=" * 30)

        show_positions()

        result = play_game(player_name)

        if result == "player":
            player_score += 1

        elif result == "ai":
            ai_score += 1

        choice = input("\nPlay Again? (y/n): ").lower()

        if choice != "y":
            print("\nFinal Score")
            print("-" * 25)
            print(f"{player_name}: {player_score}")
            print(f"AI        : {ai_score}")

            print("\n👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()