# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    
    return [f"{naam['voornaam']} {naam['tussenvoegsel']} {naam['achternaam']}".strip() for naam in lijst_met_namen]

#namenlijst
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

for naam in volledige_naam(namen):
    print(naam)