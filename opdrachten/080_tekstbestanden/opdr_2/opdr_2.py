# Opdracht 2 tekstbestanden
# Naam student:
# Groep:


import random

prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

aantal_pogingen = 0
geraden = False

while not geraden:
    try:
        gok = int(input(prompt))
        aantal_pogingen += 1

        if gok < geheim_getal:
            prompt = "Hoger! \n"
        elif gok > geheim_getal:
            prompt = "Lager! \n"
        else:
            geraden = True
            print(f"Goed geraden! Het geheime getal was {geheim_getal} en je hebt {aantal_pogingen} pogingen nodig gehad.")
    
    except ValueError:
        print("Ongeldige invoer, voer een getal in.")

# Result opslaan in een bestand
with open("resultaat.txt", "a") as file:
    file.write(f"Goed geraden! Het geheime getal was {geheim_getal} en je hebt {aantal_pogingen} pogingen nodig gehad.\n")
