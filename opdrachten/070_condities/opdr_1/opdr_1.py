# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for getal in range(1, 11):
    my_list.append(getal)

# Print alleen de getallen die groter zijn dan 4
for getal in my_list:
    if getal > 4:
        print(getal)