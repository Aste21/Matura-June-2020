def czy_pierwsza(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
def tablica():
    t = []
    for i in range(3,101):
        if czy_pierwsza(i):
            t.append(i)
    return(t)
z = tablica()
def goldbach(x):
    a = 0
    b = 0
    r = -10
    for i in range(0,len(z)):
        for j in range(i, len(z)):
            if z[i] + z[j] == x and z[j] - z[i] > r:
                a = z[i]
                b = z[j]
                r = b-a
    t = [a, b]
    return t
f = open('pary.txt', 'r')
for linia in f:
    t = linia.split()
    x = int(t[0])
    if x % 2 == 0:
        c = goldbach(x)
        print(f'{x} {c[0]} {c[1]}')