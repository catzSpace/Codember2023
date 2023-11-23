s = '1-10'



d = s.find('-')

inicio = ''
fin = ''

n = 0
for i in s:
    if n < d:
        inicio += i
    if n > d:
        fin += i
    n += 1



print(inicio)
print(fin)