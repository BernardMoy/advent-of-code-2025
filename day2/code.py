with open('input.txt', 'r') as f: 
    lines = f.read().split(',') 

# Construction of numbers, linear time 
ans = 0 
for line in lines: 
    a, b = [int(x) for x in line.split('-') ]

    # Increase a to the next repeating number 
    sa, sb = str(a), str(b) 
    if len(sa)%2 == 1: 
        low = 10**(len(sa)//2) 
    
    else: 
        x = sa[:len(sa)//2]
        y = sa[len(sa)//2:]

        if int(x)<int(y):  # e.g. 365389 -> low is 366 (for 366366)
            low = int(x)+1
        else: 
            low = int(x) # e.g. 365133 -> low is 365 (for 365365)
    
    # decrease sb to the next repeating number 
    if len(sb) % 2 ==1: 
        high = 10**((len(sb))//2)-1
    
    else: 
        x = sb[:len(sb)//2]
        y = sb[len(sb)//2:]

        if int(x)<=int(y):  # e.g. 365389 -> high is 365365
            high = int(x) 
        else: 
            high = int(x)-1 # e.g. 365133 -> high is 364 (for 364364)

    if low <= high: 
        for i in range(low, high+1): 
            ans += int(str(i)*2)
    
print(ans)



# Brute force actually works :p
def check(n): 
    s = str(n) 

    for k in range(2, len(s)+1): 
        if len(s) % k == 0: 
            if s[:len(s)//k]*k == s: 
                return True 
    
    return False 

ans2 = 0  
for line in lines: 
    a, b = [int(x) for x in line.split('-') ]

    for x in range(a,b+1): 
        if check(x): 
            ans2 += x 

print(ans2)