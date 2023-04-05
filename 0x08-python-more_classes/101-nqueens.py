#!/usr/bin/python3
"""
Thiss programme solves the N quees  problem.
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""


from sys import argv

if __name__ == "__main__":
    q = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for i in range(n):
        q.append([i, None])

    def already_exists(y):
        """check if queen does not already exist in that y value"""
        for x in range(n):
            if y == q[x][1]:
                return True
        return False

    def reject(x, y):
        """checks if or not to reject the solution"""
        if (already_exists(y)):
            return False
        i = 0

        while (i < x):
            if abs(q[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(v):
        """removes the answers from the point of failure on"""
        for i in range(v, n):
            q[i][1] = None

    def nqueens(t):
        """recursive backtracking function to find the solution"""
        for y in range(n):
            clear_a(t)
            if reject(t, y):
                q[t][1] = y
                if (t == n - 1):  # accepts the solution
                    print(q)
                else:
                    nqueens(t + 1)  # goes to next t value to continue

    # restart the recursive process again from t = 0
    nqueens(0)
