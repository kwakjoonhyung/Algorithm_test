from itertools import permutations

def solution(numbers):
    perms = []
    for i in range(1,len(numbers)+1):
        perms += list(permutations(numbers,i))
    
    
    new_perms = []
    for num in perms:
        new_perms.append(int("".join(num)))
    
        
    result = []    
    for n in new_perms:
        if n < 2:
            continue
        check = True
        for i in range(2,n):
            if n%i==0:
                check = False
                break
        if check:
            result.append(n)
            
    return len(set(result))