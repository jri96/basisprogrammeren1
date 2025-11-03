# 2Grades.py
import csv

try:
    cijfers = []
    with open("cijfers.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # sla de header over
        for row in reader:
            naam = row[0]
            vak = row[1].strip()
            opdracht = row[2].strip()
            cijfer = float(row[3])   # dit is de juiste kolom
            cijfers.append(cijfer)
            print(f"{naam} heeft het cijfer {cijfer} voor {opdracht} bij het vak {vak}")

    gemiddelde = sum(cijfers) / len(cijfers)
    with open("gemiddelde.csv", "w") as out:
        out.write(f"Gemiddelde cijfer = {gemiddelde:.2f}\n")

except FileNotFoundError:
    print("Bestand niet gevonden!")