def solution(text):
    matrix = []
    f = open(text, "r")
    for line in f:
        matrix.append(line.strip())

    directions = [[1,0],[0,1],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
    numSet = set([str(i) for i in range(10)])
    ROWS, COLS = len(matrix), len(matrix[0])
    visited = set()

    def findnum(row, col):
        l, r = col, col
        while l>=0 and matrix[row][l] in numSet:
            visited.add((row,l))
            l-=1
        while r<len(matrix[0]) and matrix[row][r] in numSet:
            visited.add((row, r))
            r+=1
        return matrix[row][l+1:r]

    ret = 0
    for row in range(ROWS):
        for col in range(COLS):
            curr = matrix[row][col]
            if curr == "*":
                # dfs
                count = 0
                ratio = 1
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if ((r,c) not in visited and
                        0<=r<ROWS and 0<=c<COLS and
                        matrix[r][c] in numSet):
                        visited.add((r,c))
                        count += 1
                        ratio *= int(findnum(r,c))
                # potential bug -> if already seen before not counted properly
                if count == 2:
                    ret += ratio
    return ret



print(solution("3.txt"))