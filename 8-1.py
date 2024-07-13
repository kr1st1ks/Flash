from itertools import permutations
alf = 'ПАЛТИН'
k = 0
for i in permutations(alf,r=5):
    s = ''.join(i)
    if 'АИ' not in s and 'ИА' not in s:
        k+=1
print(k)