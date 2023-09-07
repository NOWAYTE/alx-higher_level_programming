#!/usr/bin/python3
""" N queens puzzle """
import sys

def is_safe(board, row, col):
    # Check if it is safe to place a queen at board[row][col]
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    # Base case: If all queens are placed, print the solution
    if col >= N:
        print_solution(board)
        return True

    # Recursive backtracking to place queens in each row of the current column
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, col + 1)
            board[row][col] = 0

def print_solution(board):
    # Print the board configuration
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                sys.stdout.write("Q ")
            else:
                sys.stdout.write(". ")
        sys.stdout.write("\n")
    sys.stdout.write("\n")

# Main program
if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: nqueens N\n")
        sys.exit(1)

    # Get the value of N from the command-line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        sys.stderr.write("N must be a number\n")
        sys.exit(1)

    # Check the value of N
    if N < 4:
        sys.stderr.write("N must be at least 4\n")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0] * N for _ in range(N)]

    # Solve the N-queens problem and print all solutions
    solve_nqueens(board, 0)
