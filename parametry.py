'''
pocet_radku = 9
pocet_sloupcu = 9
oblasti = []
'''

radky0 = []
for i in range(9):
    novy_radek = []
    for j in range(9):
        novy_radek.append(i * 9 + j)
    radky0.append(novy_radek)

sloupce0 = []
for i in range(9):
    novy_sloupec = []
    for j in range(9):
        novy_sloupec.append(i + j * 9)
    sloupce0.append(novy_sloupec)

ctverce0 = []
for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
    novy_ctverec = []
    for j in range(3):
        for k in range(3):
            novy_ctverec.append(j * 9 + k + i)
    ctverce0.append(novy_ctverec)

sloupce = sloupce0
radky = radky0
ctverce = ctverce0