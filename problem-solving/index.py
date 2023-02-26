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

# print(anagram('xyyx'))

def makingAnagrams(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    i = 0
    while i < len(s1):
        if s1[i] in s2:
            s2.remove(s1[i])
            s1.remove(s1[i])
            continue
        i += 1
    return len(s1) + len(s2)

# print(makingAnagrams('abc', 'amnop'))