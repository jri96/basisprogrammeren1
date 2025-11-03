# Week 02 - Control Flow (if-statements en booleans)

# === Uitleg ===
# Met 'if' kun je beslissingen maken in je programma.

leeftijd = int(input("Hoe oud ben je? "))

if leeftijd >= 18:
    print("Je bent volwassen.")
else:
    print("Je bent minderjarig.")

# === Oefening 1 ===
# Vraag de gebruiker om een leeftijd met input() en print of iemand mag stemmen (18 jaar en ouder).
leeftijd = int(input("Wat is je leeftijd? "))

if leeftijd >= 18:
    print("Je mag stemmen.")
else:
    print("Je mag nog niet stemmen.")

# === Oefening 2 ===
# Maak een script dat controleert of een getal positief, negatief of nul is.
getal = int(input("Geef een getal: "))

if getal > 0:
    print("Het getal is positief.")
elif getal < 0:
    print("Het getal is negatief.")
else:
    print("Het getal is nul.")

# === Reflectie ===
# Wat was lastig aan het werken met beslissingen in de code?
# Schrijf op wat je nog wilt leren over if-statements.
