# Opdracht 1 while-loops
# Naam student:
# Groep:

# De vragen in een lijst
try:
# Stel de vragen
    firstquest = str(input("Wat vind je van de huidige regering: "))
    secondquest = str(input("Wat vind je van de Python-lessen tot nu toe?"))
    thirdquest = str(input("Wat vind je de mooiste stad van Nederland?"))
 
# Open een nieuw bestand in de directory van het .py bestand
    file = open("antwoorden.txt", "w")
# Schrijf de antwoorden van de vragen in het bestand
    file.write("Wat vind je van de huidige regering: " + str(firstquest) + "\n")
    file.write("Wat vind je van de Python-lessen tot nu toe: " + str(secondquest) + "\n")
    file.write("Wat vind je de mooiste stad van Nederland: " + str(thirdquest) + "\n")
 
# Error handling
except ValueError:
    print("Ongeldige invoer, probeer opnieuw.")