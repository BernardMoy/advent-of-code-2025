with open('input.txt', 'r') as f: 
    lines = f.read().split('\n\n')
    ranges = lines[0].split('\n')
    nums = lines[1].split('\n')[:-1]

import bisect 
from collections import defaultdict

# preprocess the data 
ranges = [[int(r.split('-')[0]), int(r.split('-')[1])] for r in ranges]
nums = [int(x) for x in nums] 
ranges.sort(key = lambda x: x[0]) 

# standard way to merge ranges 
merged = [] 
for start, end in ranges: 
    if not merged or merged[-1][-1] < start: 
        merged.append([start, end]) 
    else: 
        merged[-1][-1] = max(merged[-1][-1], end) 

d = {} 
for a,b in merged: 
    d[a] = b 

# Binary search the range to check 
keys = sorted(list(d.keys()))
ans = 0
for n in nums: 
    pos = bisect.bisect_left(keys, n) 

    if pos != 0: 
        start = keys[pos-1] 
        end = d[start]

        if start <= n and n <= end: 
            ans += 1 

print(ans)

ans2 = 0 
for a, b in merged: 
    ans2 += b-a+1 

print(ans2)
