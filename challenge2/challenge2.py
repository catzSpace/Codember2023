simbols = input(': ')

n = 0

for i in simbols:
    if i == '#':
        n += 1
    if i == '@':
        n -= 1
    if i == '*':
        n *= n
    if i == '&':
        print(n, end='', flush=True)