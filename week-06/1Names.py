# 1Names.py

with open("namen.txt", "r") as bestand:
    namen = [regel.strip() for regel in bestand]

for naam in namen:
    print(f"Hallo {naam}")

aantal = len(namen)

with open("resultaat.txt", "w") as out:
    out.write(f"Aantal namen = {aantal}\n")