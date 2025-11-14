mijn_spellen = []
class spellen():
    def __init__(self, spel, prijs):
        self.spel = spel
        self.prijs = prijs

    def print_spel_prijs(self):
        print(f"{self.spel}, {self.prijs}")

    def prijs_optel(self):
        return self.prijs

while True:
    print("1)Spellen bekijken")
    print("2)Spel toevoegen")
    print("3)Totaalprijs berekenen")
    print("4)Afsluiten")

    gg = int(input(""))
    if gg == 1:
        print()
        for div1 in range(len(mijn_spellen)):
            mijn_spellen[div1].print_spel_prijs()
        print()

    elif gg == 2:
        spel = input("Hoe heet het spel dat je wilt toevoegen? ")
        prijs = input("En hoe duur is het spel? ")
        mijn_spellen.append(spellen(spel, prijs))
        print()
        
    elif gg == 3:
        div3 = 0
        for div2 in range(len(mijn_spellen)):
            div3 = div3 + int(mijn_spellen[div2].prijs_optel())
        print(div3)
        print()
            
    elif gg == 4:
        break

    elif gg > 4:
        print()
        print("Ongeldige invoer")
        print()