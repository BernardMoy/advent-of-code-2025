with open('input.txt', 'r') as f: 
    lines = f.read().split('\n\n')

import copy 

def to_index(grid): 
    grid = grid.split('\n')
    a = [] 
    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            if grid[i][j] == '#': 
                a.append((i,j)) 
    
    return a 

def normalise(pattern):
    minx = min(x for x,y in pattern)
    miny = min(y for x,y in pattern)
    return [(x - minx, y - miny) for x,y in pattern]

def rotate(pattern):
    return [(-y, x) for x, y in pattern]

def flip(pattern):
    return [(-x, y) for x, y in pattern]

def generate_orientations(pattern):
    visited = set() 
    patterns = []

    r0 = pattern
    r1 = rotate(pattern) 
    r2 = rotate(r1) 
    r3 = rotate(r2)
    r1f = flip(r1) 
    r2f = flip(r2) 
    r3f = flip(r3) 

    for r in [r0, r1, r2, r3, r1f, r2f, r3f]: 
        n = normalise(r)
        s = tuple(sorted(n))
        if s in visited: 
            continue 

        patterns.append(n) 
        visited.add(s) 
    
    return patterns 

visited = set() 
def valid(grid, counts): 
    state = (tuple(map(tuple, grid)), tuple(sorted(counts.items())))

    if state in visited:
        return False
    
    # return true when counts dictionary is empty 
    if not counts: 
        return True 

    for key, value in counts.items(): 
        # Resurcive counts dictionary 
        new_counts = copy.deepcopy(counts)
        new_counts[key] = value - 1 
        if new_counts[key] == 0: 
            del new_counts[key] 

        # find all patterns to check 
        patterns = generate_orientations(d[key]) 

        for x in range(len(grid)-2): 
            for y in range(len(grid[0])-2): 
                for pattern in patterns: 
                        # generate the new grid 
                        new_grid = copy.deepcopy(grid)
                        ok = True 

                        # Simulate setting all those bits to 1 
                        for i,j in pattern: 
                            # if already 1, cant place pattern on top 
                            if new_grid[x+i][y+j] == 1: 
                                ok = False
                                break 

                            new_grid[x+i][y+j] = 1 
                        
                        # Recursively call 
                        if ok and valid(new_grid, new_counts): 
                            return True 
    
    
    return False 



d = {} 
grids = lines[:-1]
for g in grids: 
    a,b = g.split(':\n')[0], g.split(':\n')[1] 
    d[int(a)] = (to_index(b)) 

queries = lines[-1].split('\n')[:-1] 
ans = 0
for q in queries: 
    t = q.split(': ')[0].split('x')
    grid = [[0 for _ in range(int(t[1]))] for _ in range(int(t[0]))]
    counts = {} 
    t2 = q.split(': ')[1].split(' ')
    for i in range(len(t2)): 
        if t2[i] != '0': 
            counts[i] = int(t2[i])
    print(grid, counts)
    if valid(grid, counts): 
        ans += 1 
        print(ans)

print(ans)
