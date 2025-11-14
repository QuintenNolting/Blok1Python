class Kaart:
    def __init__(self, naam, waarde, aas=False):
        self.naam = naam
        self.waarde = waarde
        self.aas = aas

    def kaartenreturn(self):
        return f"{self.naam} == {self.waarde}"
    
    def is_aas(self):
        return self.aas
    
    def kies_waarde(self):
        while True:
            inputwaardeaas = int(input("Kies de waarde van de aas, 1 of 10. "))
            if inputwaardeaas == 1:
                self.waarde = 1
                break
            elif inputwaardeaas == 10:
                self.waarde = 10
                break
    
    def aasisgekozen(self):
        self.aas = False
            

class Deler:
    def __init__(self):
        self.hand = []

    def voeg_toe_deler(self, kaart):
        self.hand.append(kaart)

    def delershand(self):
        for kaart in self.hand:
            print(kaart.kaartenreturn())

    def totaalkaartendeler(self):
        totaal = 0
        for kaart in self.hand:
            totaal = totaal + kaart.waarde
        return totaal

class Speler:
    def __init__(self):
        self.hand = []

    def voeg_toe_speler(self, kaart):
        self.hand.append(kaart)

    def spelershand(self):
        for kaart in self.hand:
            print(kaart.kaartenreturn())

    def geefhandspeler(self):
        return self.hand
            
    def totaalkaartenspeler(self):
        totaal = 0
        for kaart in self.hand:
            totaal = totaal + kaart.waarde
        return totaal

def maak_deck():
    return [Kaart("\u2660\uFE0F 2", 2),
            Kaart("\u2660\uFE0F 3", 3),
            Kaart("\u2660\uFE0F 4", 4),
            Kaart("\u2660\uFE0F 5", 5),
            Kaart("\u2660\uFE0F 6", 6),
            Kaart("\u2660\uFE0F 7", 7),
            Kaart("\u2660\uFE0F 8", 8),
            Kaart("\u2660\uFE0F 9", 9),
            Kaart("\u2660\uFE0F 10", 10),
            Kaart("\u2660\uFE0F aas", 10, True),
            Kaart("\u2660\uFE0F heer", 10),
            Kaart("\u2660\uFE0F dame", 10),
            Kaart("\u2660\uFE0F boer", 10),
            Kaart("\u2764\uFE0F 2", 2),
            Kaart("\u2764\uFE0F 3", 3),
            Kaart("\u2764\uFE0F 4", 4),
            Kaart("\u2764\uFE0F 5", 5),
            Kaart("\u2764\uFE0F 6", 6),
            Kaart("\u2764\uFE0F 7", 7),
            Kaart("\u2764\uFE0F 8", 8),
            Kaart("\u2764\uFE0F 9", 9),
            Kaart("\u2764\uFE0F 10", 10),
            Kaart("\u2764\uFE0F aas", 10, True),
            Kaart("\u2764\uFE0F heer", 10),
            Kaart("\u2764\uFE0F dame", 10),
            Kaart("\u2764\uFE0F boer", 10),
            Kaart("\u2666\uFE0F	2", 2),
            Kaart("\u2666\uFE0F 3", 3),
            Kaart("\u2666\uFE0F 4", 4),
            Kaart("\u2666\uFE0F 5", 5),
            Kaart("\u2666\uFE0F 6", 6),
            Kaart("\u2666\uFE0F 7", 7),
            Kaart("\u2666\uFE0F 8", 8),
            Kaart("\u2666\uFE0F 9", 9),
            Kaart("\u2666\uFE0F 10", 10),
            Kaart("\u2666\uFE0F aas", 10, True),
            Kaart("\u2666\uFE0F heer", 10),
            Kaart("\u2666\uFE0F dame", 10),
            Kaart("\u2666\uFE0F boer", 10),
            Kaart("\u2663\uFE0F 2", 2),
            Kaart("\u2663\uFE0F 3", 3),
            Kaart("\u2663\uFE0F 4", 4),
            Kaart("\u2663\uFE0F 5", 5),
            Kaart("\u2663\uFE0F 6", 6),
            Kaart("\u2663\uFE0F 7", 7),
            Kaart("\u2663\uFE0F 8", 8),
            Kaart("\u2663\uFE0F 9", 9),
            Kaart("\u2663\uFE0F 10", 10),
            Kaart("\u2663\uFE0F aas", 10, True),
            Kaart("\u2663\uFE0F heer", 10),
            Kaart("\u2663\uFE0F dame", 10),
            Kaart("\u2663\uFE0F boer", 10)]