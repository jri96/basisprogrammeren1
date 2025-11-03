# lees challenge 5 in Canvas voor de opdracht

# Dictionary voor het menu
menu = {
    "pizza": 8.50,
    "pasta": 7.00,
    "salade": 5.50,
    "soep": 4.00,
    "burger": 9.00
}

# Functie om het menu te tonen
def toon_menu():
    print("=== Menu ===")
    for gerecht, prijs in menu.items():
        print(f"{gerecht} - €{prijs:.2f}")
    print("============")

# Functie om bestelling op te nemen
def neem_bestelling_op():
    bestelling = {}
    while True:
        keuze = input("Wat wilt u bestellen? ").lower()
        if keuze == "klaar":
            break
        elif keuze in menu:
            bestelling[keuze] = bestelling.get(keuze, 0) + 1
            print(f"{keuze} toegevoegd aan bestelling.")
        else:
            print(f"'{keuze}' staat niet op het menu!")
    return bestelling

# Functie om totaalprijs te berekenen en rekening te tonen
def bereken_rekening(bestelling):
    print("\n=== Uw rekening ===")
    totaal = 0.0
    for gerecht, aantal in bestelling.items():
        prijs = menu[gerecht] * aantal
        totaal += prijs
        print(f"{gerecht} x{aantal} - €{prijs:.2f}")
    print("-------------------")
    print(f"Totaal: €{totaal:.2f}")

# Main functie
def main():
    toon_menu()
    bestelling = neem_bestelling_op()
    bereken_rekening(bestelling)

# Start het programma
if __name__ == "__main__":
    main()