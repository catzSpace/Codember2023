strs = str(input(': '))

res = strs.split()

word = ''
n = 0
rep = []


for i in res:
    if i not in rep:
        for j in res:
            word = i.lower()
            if word == j.lower():
                n += 1
                rep.append(word)
        print(f'{word}{n}', end='', flush=True)
        n = 0