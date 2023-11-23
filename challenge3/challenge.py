#str
lista = []

#multiple linea
while True:
    e = input()
    if e.strip():
        lista.append(e)
    else:
        break

#variables/datos necesarios
r = []
rango = ''
l = []
letra = ''
p = []
password = ''


#extractor y separador
def separar(dato):
    n = 0
    separacion = dato.split()
    for j in separacion:
            n += 1

            if n == 1:
                r.append(j)
            if n == 2:
                l.append(j)
            if n == 3:
                p.append(j)
            
    n = 0


#contador de resultados
count = 0


#ejecucion
for dato in lista:

    separar(dato)

    #convertir en str
    for i in l:
        for j in i:
            if j != ':':
                letra += j
    
    for i in r:
        for j in i:
            rango += j
    
    for i in p:
        for j in i:
            password += j

    #inicio y final (rango)
    intervalo = rango.find('-')
    inicio = ''
    fin = ''
    n = 0
    for i in rango:
        if n < intervalo:
            inicio += i
        if n > intervalo:
            fin += i
        n += 1

    #resultado
    n = 0
    for i in password:
        if i == letra:
            n += 1
    if n < int(inicio) or n > int(fin):
        count += 1
        print(f'{count}. {password}') #mostrar resultados numerados

    #formatear variables
    rango = ''
    r.clear()
    password = ''
    p.clear()
    letra = ''
    l.clear()
    inicio = ''
    fin = ''