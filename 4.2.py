f = open('przyklad.txt', 'r')
for linia in f:
    t = linia.split()
    x = t[1]
    p = [x[0]]
    z = [x[0]]
    fragment_p = True
    for i in range(1,len(x)):
        if x[i] == p[0] and fragment_p:
            p.append(x[i])
        elif x[i] != p[0] and x[i] == z[0]:
            z.append(x[i])
        elif x[i] != p[0] and x[i] != z[0]:
            z.clear()
            z.append(x[i])
            fragment_p = False
        if len(z) > len(p):
            p = z
            fragment_p = True
    print(f"{''.join(p)} {len(p)}")
    break