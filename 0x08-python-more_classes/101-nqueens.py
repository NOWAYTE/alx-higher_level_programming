#!/usr/bin/python3
def print_solution(board):
    # Print the board configuration as a string
    solution = []
    for i in range(N):
        row = []
        for j in range(N):
            if board[i][j] == 1:
                row.append("Q")
            else:
                row.append(".")
        solution.append("".join(row))
    print(solution)
