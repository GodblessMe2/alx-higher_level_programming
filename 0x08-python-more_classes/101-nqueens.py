#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""
from sys import argv

if __name__ == "__main__":
    a = []
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

    #Initialise the answer list
    for i in range(n):
        a.append([i, None])

    def already_exist(y):
        """Check that a queen does not already exist in that y value"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False
    
    def reject(x, y):
        """if exist reject else continue"""
        if (already_exist(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True
    
    def clear_a(x):
        """Clear the answers if failure is on"""
        for c in range(x, n):
            a[c][1] = None
    
    def noqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(n):
            clear_a(x)
        if reject(x, y):
            a[x][1] = y
            if (x == n - 1):
                print(a)
            else:
                noqueens(x + 1)
    # start the recursive process at x = 0
    noqueens(0)
