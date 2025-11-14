import berekeningen

while True:
    h = input("Wil je een berekening doen? Ja of nee? ")
    if h == "nee":
        print("Als je weer verder wilt zeg dan ja hieronder.")
    elif h == "ja":
        bb = input("Welke berekening wil je doen? Optellen, aftrekken, vermenigvuldigen of delen? ")

        if bb == "optellen":
            getal1 = int(input("Voer het eerste getal in. "))
            getal2 = int(input("Voer het tweede getal in. "))
            resultaat1 = berekeningen.optellen(getal1, getal2)
            print("Resultaat:", resultaat1)

        elif bb == "aftrekken":
            getal1 = int(input("Voer het eerste getal in. "))
            getal2 = int(input("Voer het tweede getal in. "))
            resultaat1 = berekeningen.aftrekken(getal1, getal2)
            print("Resultaat:", resultaat1)

        elif bb == "vermenigvuldigen":
            getal1 = int(input("Voer het eerste getal in. "))
            getal2 = int(input("Voer het tweede getal in. "))
            resultaat1 = berekeningen.vermenigvuldigen(getal1, getal2)
            print("Resultaat:", resultaat1)
            
        elif bb == "delen":
            getal1 = int(input("Voer het eerste getal in. "))
            getal2 = int(input("Voer het tweede getal in. "))
            
            while getal2 == 0:
                print("Je mag niet door nul delen.")
                getal2 =int(input("Voer het tweede getal opnieuw in, het mag niet nul zijn. "))
            else:
                resultaat1 = berekeningen.delen(getal1, getal2)
                print("Resultaat:", resultaat1)