import spel_onderdelen
import random
breakbreak = True
print()
print("De regels voor blackjack:")
print("Aan het begin pakt de deler 2 kaarten.")
print("Je mag zoveel kaarten pakken als je wilt.")
print("Je wint als je de meeste punten hebt of 21 punten.")
print("Als je meer dan 21 punten hebt heb je verloren.")
print()
regels_klaar = input("Klaar met de regels lezen? [ENTER]")
print()
while breakbreak:
    print()
    print("Het spel begint nu!")
    kaarten = spel_onderdelen.maak_deck()
    random.shuffle(kaarten)

    print("##########################")
    print("De deler pakt 2 kaarten.")
    Deler = spel_onderdelen.Deler()
    Deler.voeg_toe_deler(kaarten.pop())
    Deler.voeg_toe_deler(kaarten.pop())
    Deler.delershand()
    print("##########################")
    totaaldeler = Deler.totaalkaartendeler()
    print("Totaal:" , totaaldeler)
    print("##########################")


    print()


    print("##########################")
    print("De speler pakt 2 kaarten.")
    Speler = spel_onderdelen.Speler()
    Speler.voeg_toe_speler(kaarten.pop())
    Speler.voeg_toe_speler(kaarten.pop())
    Speler.spelershand()
    print("##########################")
    totaalspeler = Speler.totaalkaartenspeler()
    print("Totaal:" , totaalspeler)
    print("##########################")
    print()

    for op in Speler.geefhandspeler():
            if op.is_aas():
                op.kies_waarde()
                op.aasisgekozen()
                totaalspeler = Speler.totaalkaartenspeler()
                Speler.spelershand()
                print("##########################")
                totaalspeler = Speler.totaalkaartenspeler()
                print("Totaal:" , totaalspeler)
                print("##########################")
                print()

    while breakbreak:
        hitcall = input("HIT[1] or CALL[2]? ")
        if hitcall == "2":
            while True:
                if totaaldeler <= 16:
                    Deler.voeg_toe_deler(kaarten.pop())
                    totaaldeler = Deler.totaalkaartendeler()
                else:
                    break
            if totaaldeler >= 22:
                print()
                print("Je hebt gewonnen!")
                print("De deler heeft meer dan 21.")
                print()
                print("Jouw totaal:" , totaalspeler)
                print("Deler's totaal:" , totaaldeler)
                print()
                break

            elif totaalspeler == totaaldeler:
                print()
                print("Het is gelijkspel.")
                print()
                print("Jouw totaal:" , totaalspeler)
                print("Deler's totaal:" , totaaldeler)
                print()
                break
                    
            elif totaalspeler > totaaldeler:
                print()
                print("Je hebt gewonnen!")
                print()
                print("Jouw totaal:" , totaalspeler)
                print("Deler's totaal:" , totaaldeler)
                print()
                break

            elif totaalspeler < totaaldeler:
                print()
                print("Je hebt verloren.")
                print()
                print("Jouw totaal:" , totaalspeler)
                print("Deler's totaal:" , totaaldeler)
                print()
                break


        if hitcall == "1":
            print()
            print("##########################")
            print("Deler's kaarten")
            Deler.delershand()
            print("##########################")
            print("Totaal:" , totaaldeler)
            print("##########################")

            print()

            print("##########################")
            print("De speler pakt een kaart.")
            Speler.voeg_toe_speler(kaarten.pop())
            Speler.spelershand()
            print("##########################")
            totaalspeler = Speler.totaalkaartenspeler()
            print("Totaal:" , totaalspeler)
            print("##########################")
            print()
            for op in Speler.geefhandspeler():
                if op.is_aas():
                    op.kies_waarde()
                    op.aasisgekozen()
                    totaalspeler = Speler.totaalkaartenspeler()
            Speler.spelershand()
            print("##########################")
            totaalspeler = Speler.totaalkaartenspeler()
            print("Totaal:" , totaalspeler)
            print("##########################")

            if totaalspeler >= 22:
                print()
                print("Je hebt verloren,")
                print("je hebt meer dan 21.")
                print()
                print("Jouw totaal:" , totaalspeler)
                print("Deler's totaal:" , totaaldeler)
                print()
                break   

            if totaalspeler == 21:
                print()
                print("Je hebt gewonnen!")
                print("21 gehaald.")
                print()
                print("Jouw totaal:" , totaalspeler)
                print("Deler's totaal:" , totaaldeler)
                print()
                break
                
    print("==============================")
    while True:
        Nogeenronde = input("Wil je nog een ronde spelen, ja of nee? ")
        if Nogeenronde == "nee":
            breakbreak = False
            break
        elif Nogeenronde == "ja":
            break