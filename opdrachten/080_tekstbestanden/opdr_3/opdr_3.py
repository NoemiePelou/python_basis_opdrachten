# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def versleutel_tekst(tekst, verschuiving):
    versleuteld = ""
    for char in tekst:
        if char.isalpha():  # Alleen letters aanpassen
            ascii_offset = ord('A') if char.isupper() else ord('a')
            nieuwe_letter = chr((ord(char) - ascii_offset + verschuiving) % 26 + ascii_offset)
            versleuteld += nieuwe_letter
        else:
            versleuteld += char  # Spaties en leestekens blijven hetzelfde
    return versleuteld

# Vraag om invoer
invoer = input("Geef de tekst die je wilt encrypten: ")
versleutelde_tekst = versleutel_tekst(invoer, 5)
print("Versleutelde tekst:", versleutelde_tekst)

# Optioneel: Decryptie uitvoeren
ontsleutelde_tekst = versleutel_tekst(versleutelde_tekst, -5)
print("Ontsleutelde tekst:", ontsleutelde_tekst)


