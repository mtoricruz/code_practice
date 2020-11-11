# Understanding
# chess board size = n x n
# must place nqueen that doesn't fall in path of other nqueens
# initialize results list
# the permutation answers follow [col1, col2,..., coln]
    # the # in colx indicates the queen in that col is placed on that row #
# watch for explanation walkthrough: https://www.youtube.com/watch?v=xFv_Hl4B83A

# Planning
# results = []
# for row in range(0, n):
    # for col in range(0, n):
        # board = [row][col]
        # queen = 

# Execute

# Refactor/Reflection
def nQueens(n):
    def isLegal(board):
        seenRows = set()
        diffs = set()
        sums = set()
        for col, row in enumerate(board):
            if row is False:
                break
            col += 1

            if row in seenRows:
                return False
            seenRows.add(row)

            diff = col-row
            if diff in diffs:
                return False
            diffs.add(diff)

            s = col+row
            if s in sums:
                return False
            sums.add(s)
        return True
    results = []

    def placeNext(boardSoFar):
        try:
            idx = boardSoFar.index(False)
        except ValueError:
            results.append(boardSoFar)
        else:
            for guess in range(1, n+1):
                boardSoFar = boardSoFar[:]
                boardSoFar[idx] = guess
                if isLegal(boardSoFar):
                    placeNext(boardSoFar)
    board = [False]*n
    placeNext(board)
    return results