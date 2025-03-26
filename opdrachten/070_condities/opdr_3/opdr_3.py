# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijdgrenzen = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

leeftijd = int(input("Geef uw leeftijd in aantal jaar\n"))

# Bepaal tot welke groep de leeftijd behoort en bereken de prijs
for groep, grenzen in leeftijdgrenzen.items():
    if grenzen[0] <= leeftijd <= grenzen[1]:
        korting = kortings_percentages[groep]
        prijs = normale_toegangsprijs * (1 - korting / 100)
        print(f"U behoort tot de groep {groep}")
        print(f"U krijgt {korting}% korting")
        print(f"U betaalt daarom {prijs:.2f}")
        break