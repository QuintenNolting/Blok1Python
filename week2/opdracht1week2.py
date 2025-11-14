"""
Opdracht 1 Week 2
Quinten Nolting
14-9-2025
Er wordt hier gebruik gemaakt van 'for' en 'while' loops om 5 rijen te maken steeds op een andere manier.
Er zijn single line comments bij de laatste van de for en while loops.
"""

for int in range(5):
    print('*****')
print()
for int in range(1, 6):
    print('*' * int)
print()
for int in range(5, 0, -1):
    print('*' * int)
print()
for int in range(5):
    for int in range(1, 6):
        print(int, end='')
    print()
print()
for int in range(6):
    for int in range(1, int + 1):
        print(int, end='')
    print()
print()
for int in range(1, 6):                # zolang het getal 1, 2, 3, 4 of 5 is zal hij verder gaan naar de volgende regel
    print('.' * (5 - int), end='')     # print puntjes om de ander cijfers weg te schuiven
    for int in range(1, int + 1):      # gaat van 1 tot en met het getal + 1
        print(int, end='')             # print het getal
    print()                            # hier gaat het een regel naar beneden
print()

print()
variabel_1 = 0
while variabel_1 < 5:
    print('*****')
    variabel_1 += 1
print()
variabel_2 = 1
while variabel_2 <= 5:
    print('*' * variabel_2)
    variabel_2 += 1
print()
variabel_3 = 5
while variabel_3 > 0:
    print('*' * variabel_3)
    variabel_3 -= 1
print()
variabel_4 = 0
while variabel_4 < 5:
    variabel_5 = 1
    while variabel_5 <= 5:
        print(variabel_5, end='')
        variabel_5 += 1
    print()
    variabel_4 += 1
print()
variabel_6 = 1
while variabel_6 <= 5:
    variabel_7 = 1
    while variabel_7 <= variabel_6:
        print(variabel_7, end='')
        variabel_7 += 1
    print()
    variabel_6 += 1
print()
variabel_8 = 1
while variabel_8 <= 5:                        # zolang variabel_8 het getal minder dan 5 is of gelijk aan zal hij verder gaan naar de volgende regel
    print('.' * (5 - variabel_8), end='')     # print puntjes om de ander cijfers weg te schuiven
    variabel_9 = 1
    while variabel_9 <= variabel_8:           # zolang variabel_9 kleiner of gelijk aan variabel_8 is zal hij verder gaan naar de volgende regel
        print(variabel_9, end='')             # print variabel_9
        variabel_9 += 1                       # variabel_9 + 1
    print()
    variabel_8 += 1                           # variabel_8 + 1
print()