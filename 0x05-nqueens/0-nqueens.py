#!/usr/bin/python3

import sys


def BruteForce(n, col, board, rows, dia, anti_dia, solutions):
    if col == n:
        solutions.append([[i, board[i].index(1)] for i in range(n)])
        return

    for row in range(n):
        if not rows[row] and not dia[row - col] and not anti_dia[row + col]:
            board[row][col] = 1
            rows[row] = True
            dia[row - col] = True
            anti_dia[row + col] = True

            BruteForce(n, col + 1, board, rows, dia, anti_dia, solutions)

            board[row][col] = 0
            rows[row] = False
            dia[row - col] = False
            anti_dia[row + col] = False


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    rows = [False] * n
    dia = [False] * (2 * n - 1)
    anti_dia = [False] * (2 * n - 1)
    solutions = []

    BruteForce(n, 0, board, rows, dia, anti_dia, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
