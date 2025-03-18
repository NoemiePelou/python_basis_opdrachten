# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Paul", "Kees", "Marie", "Hilda"]
gasten.insert(0, "Jij")
print("Beginnende gastenlijst:", gasten)

gasten.remove("Marie")
print("Gastenlijst zonder Marie:", gasten)

index_kees = gasten.index("Kees")
gasten.insert(index_kees +1, "George")
print("Gastenlijst met George naast Kees:", gasten)