f = open('pary.txt', 'r')
t = []
for linia in f:
    c = linia.split()
    a = int(c[0])
    b = c[1]
    if a == len(b):
        z = [a, b]
        t.append(z)
while len(t) > 1:
    if t[0][0] > t[1][0]:
        t.pop(0)
    elif t[0][0] < t[1][0]:
        t.pop(1)
    elif t[0][0] == t[1][0] and t[0][1] > t[1][1]:
        t.pop(0)
    else:
        t.pop(1)
print(f"{t[0][0]} {t[0][1]}")

