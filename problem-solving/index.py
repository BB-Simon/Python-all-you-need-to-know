def anagram(s):
    if len(s) %2 != 0:
        return -1
    
    a = [*s[:len(s)//2]]
    b = [*s[len(s)//2:]]
    c = 0
    for i in a:
        if i not in b:
            c += 1
        else:
            b.remove(i)    
    return c

print(anagram('xyyx'))