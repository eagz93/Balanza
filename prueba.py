### Juego de tic tac-toe en Python
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def main():
    # Initialize the game
    board = [[" ", " ", " "] for _ in range(3)]
    current_player = random.choice(["X", "O"])

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"¡El jugador {winner} ha ganado!")
            break
        if is_board_full(board):
            print("¡Es un empate!")
            break

        print(f"Turno del jugador {current_player}")
        try:
            row = int(input("Ingrese la fila (0-2): "))
            col = int(input("Ingrese la columna (0-2): "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números.")
            continue

        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = current_player
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Esa posición ya está ocupada.")
        else:
            print("Posición fuera de los límites. Ingrese valores entre 0 y 2.")

if __name__ == "__main__":
    main()