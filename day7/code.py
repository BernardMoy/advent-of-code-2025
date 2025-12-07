with open('input.txt', 'r') as f: 
    lines = f.read().split('\n')[:-1]
from collections import defaultdict

# Given: The ^ and . must alternate, and no ^ can be on the edges. 
initial = lines[0].find('S')
times = [0]*len(lines[0])
times[initial] = 1 
s = set([initial]) 
ans = 0 
for i in range(1, len(lines)): 
    for j in range(len(lines[i])): 
        if lines[i][j] == '^':
            # Split beams into two  
            if j in s: 
                s.remove(j)
                s.add(j-1) 
                s.add(j+1)
                ans += 1 
                times[j-1] += times[j]   # Prefix addition 
                times[j+1] += times[j] 
                times[j] = 0 

print(ans)

print(sum(times))