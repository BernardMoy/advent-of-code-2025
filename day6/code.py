with open('input.txt', 'r') as f: 
    lines = f.read().split('\n')[:-1]

import re
nums = lines[:-1]
ops = lines[-1] 
ops = re.sub(r'\s+', '', ops)

cur = []
for line in nums: 
    line = re.sub(r'\s+', ' ', line)
    line = [int(x) for x in line.strip().split(' ')]
    if not cur: 
        cur = line
    
    else: 
        for i in range(len(line)): 
            if ops[i] == '+': 
                cur[i] += line[i] 
            else: 
                cur[i] *= line[i] 

print(sum(cur))



# for part 2 iterate each column 
curop = '+'
ans2 = []   # not necessary
cur = 0 
for col in range(len(lines[0])): 
    n = ''
    for row in range(len(lines)): 
        if lines[row][col] == '+': 
            cur = 0
            curop = '+' 
        elif lines[row][col] == '*': 
            cur = 1
            curop = '*'
        elif lines[row][col] != ' ': 
            n += (lines[row][col])
        
        
    # now we have the column number 
    if n != '': 
        if curop == '+': 
            cur += int(n) 
        elif curop == '*': 
            cur *= int(n) 

    else: 
        ans2.append(cur) 

ans2.append(cur) 
print(sum(ans2))