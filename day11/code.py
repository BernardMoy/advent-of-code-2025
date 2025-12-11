with open('input.txt', 'r') as f: 
    lines = f.read().split('\n')[:-1]

d = {} 

for line in lines: 
    left, right = line.split(': ')[0], line.split(': ')[1] 
    d[left] = right.split(' ')


# Simple DFS for part 1 
def dfs(start): 
    if start == 'out': 
        return 1 

    count = 0 
    for nei in d[start]: 
        count += dfs(nei) 
    
    return count 

print(dfs('you'))


# Somehow the provided graph may contain CYCLES. 
def dfs2(start, dac, fft, visited = {}): 
    if ((start, dac, fft)) in visited: 
        return visited[(start, dac, fft)]
    if start == 'out' and dac and fft: 
        return 1 
    if start == 'out': 
        return 0 

    count = 0 
    for nei in d[start]: 
        count += dfs2(nei, nei == 'dac' or dac, nei == 'fft' or fft, visited) 
    
    visited[(start, dac, fft)] = count 
    return count 

# Why is the answer so large !?
print(dfs2('svr', False, False))