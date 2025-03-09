def n_queen(n):
    def check_position(board, row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if check_position(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * n
    solutions = []
    backtrack(0)

    return solutions

def print_solutions(solutions, n):
    for sol in solutions:
        for row in range(n):
            line = ['.'] * n
            line[sol[row]] = 'Q'
            print(' '.join(line))
        print()

n = int(input("Enter the size of the grid (N): "))
if n < 1:
    print("Invalid input! N must be a positive integer.")
else:
    all_solutions = n_queen(n)
    print(f"Total solutions for {n}-Queens: {len(all_solutions)}")
    if all_solutions:
        print_solutions(all_solutions, n)