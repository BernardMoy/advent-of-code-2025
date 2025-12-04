with open('input.txt', 'r') as f: 
    lines = [list(x) for x in f.read().split('\n')[:-1]]

def valid(grid,i,j): 
    count = 0 
    ROWS, COLS = len(grid), len(grid[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for a,b in directions: 
        ni, nj = i+a, j+b 
        if 0<=ni<ROWS and 0<=nj<COLS and grid[ni][nj] == '@': 
            count += 1 
    
    return count <4

ans = 0 
s = set() 
for i in range(len(lines)): 
    for j in range(len(lines)): 
        if lines[i][j] == '@' and valid(lines, i, j): 
            s.add((i,j))
            ans += 1 

print(ans)


# While set has elements, remove all the papers inside it 
while s: 
    for a,b in s: 
        lines[a][b] = '.'

    # Clear the set every time 
    s.clear() 
    for i in range(len(lines)): 
        for j in range(len(lines)): 
            if lines[i][j] == '@' and valid(lines, i, j): 
                s.add((i,j))
                ans += 1 

print(ans)