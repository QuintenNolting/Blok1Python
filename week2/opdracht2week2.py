"""
Opdracht 1 Week 2
Quinten Nolting
14-9-2025
Er wordt hier een vierkant gemaakt door vragen te stellen hoe groot en waarvan het moet worden gemaakt.
"""
getal = int(input("Hoe groot moet het vierkant zijn? "))
buiten_symbool = input("Welk symbool heeft de buitenkant? ")
binnen_symbool = input("Welk symbool heeft de binnenkant? ")

for i in range(getal):                                                           # zolang het getal niet meer is dan wat er geantwoord werdt is gaat hij naar de volgende regel
    if i == 0 or i == getal - 1:                                                 # eerste of laatste regel
        print(buiten_symbool * getal)                                            # print een rij van het buiten_symbool
    else:                                                                        # de andere regels
        print(buiten_symbool + binnen_symbool * (getal - 2) + buiten_symbool)    # print buiten_symbool met binnen_symbool ertussen
