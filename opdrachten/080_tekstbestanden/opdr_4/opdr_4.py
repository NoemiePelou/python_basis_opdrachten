# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
def feestganger_vragen():
    vragen = [
        "Wat is je voornaam?",
        "Wat is je achternaam?",
        "Wat neem je mee aan drank?",
        "Wat neem je mee om te eten?"
    ]
    
    feestgangers = []
    while True:
        antwoorden = {}
        for i, vraag in enumerate(vragen, 1):
            antwoord = input(f"{i}. {vraag} ")
            if i == 1:
                antwoorden["voornaam"] = antwoord
            elif i == 2:
                antwoorden["achternaam"] = antwoord
            elif i == 3:
                antwoorden["drank"] = antwoord
            elif i == 4:
                antwoorden["eten"] = antwoord
        
        feestgangers.append(antwoorden)
        print("\nBedankt voor het invullen! Tot op het feest!\n")
        
        verder = input("Wil je nog een feestganger invoeren? (ja/nee): ").strip().lower()
        if verder != "ja":
            break
    
    # Opslaan in tekstbestand
    with open("feestgangers.txt", "a") as file:
        for gast in feestgangers:
            file.write("----\n")
            for key, value in gast.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
    
    print("Alle gegevens zijn opgeslagen in 'feestgangers.txt'.")

# Start het programma
feestganger_vragen()