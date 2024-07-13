from itertools import permutations
alf = 'МЕЖГЛКТИЧСЯ'
k = 0
for i in permutations(alf,r=6):
    s = ''.join(i)
    if s[0] in 'МЖГЛКТЧС' and s[1] in 'МЖГЛКТЧС' and s[-2] in 'ЕИЯ' and s[-1] in 'ЕИЯ':
        if s[2] in 'ЕИЯ' and s[3] in 'МЖГЛКТЧС':
            k+=1
print(k)