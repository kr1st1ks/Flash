from itertools import permutations
alf = 'САЙУОЕР'
k = 0
for i in permutations(alf,r=6):
    s = ''.join(i)
    if s[0] in 'СРЙ' and s[-1] in 'АУОЕ':
        s1 = s
        s1 = s1.replace('Р','С')
        s1 = s1.replace('Й','С')
        if 'СС' not in s:
            k+=1
print(k)