with open('input.txt', 'r') as f: 
    lines = f.read().split('\n')[:-1]

def find(s): 
    # Find the largest leftmost value except the last one 
    cur = -1 
    ind = -1
    for i in range(len(s)-1): 
        if int(s[i]) > cur: 
            cur = int(s[i])
            ind = i 
    
    # Find the second largest value from i onwards 
    cur2 = -1 
    for j in range(ind+1, len(s)): 
        cur2 = max(cur2, int(s[j])) 
        
    return cur*10+cur2

ans = 0 
for line in lines: 
    ans += find(line) 

print(ans)




# Alternatively, use recursion for lengths more than 2. 
def rec_find(s, n): 
    if len(s) == 0 or n == 0: 
        return '' 
    
    # Must reserve at least n spaces for later use 
    valid = s[:len(s)-n+1] 
    cur = max(valid) 
    ind = s.find(cur) 

    return cur + rec_find(s[ind+1:], n-1) 

ans2 = 0 
for line in lines: 
    ans2 += int(rec_find(line, 12)) 

print(ans2)