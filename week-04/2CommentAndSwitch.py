#Hier voer je de getallen in die je wilt berekenen
getal1 = float(input("Getal 1: "))
getal2 = float(input("Getal 2: "))

#Vraag welke berekening uitgevoerd moet worden
bewerking = input("Welke berekening wil je? (plus, min, keer, deel): ").lower()

#Hier zorg je ervoor wat je kiest dat dat uitgerekent word
if bewerking == "plus":
    Uitkomst = getal1 + getal2
elif bewerking == "min":
    Uitkomst = getal1 - getal2
elif bewerking == "keer":
    Uitkomst = getal1 * getal2
elif bewerking == "deel":
    if getal2 != 0:
        Uitkomst = getal1 / getal2
    else:
        Uitkomst = "Fout: delen door nul!"
else:
    Uitkomst = "Onbekende berekening"

#Hier komt het eind resultaat
print("Uitkomst:", Uitkomst)