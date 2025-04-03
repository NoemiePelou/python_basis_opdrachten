# Opdracht 1 functies
# Naam student:
# Groep:


import math

#Bereken het vulme van een kubus
def kubus_vol(zijde):
    return zijde ** 3

#Bereken het volume van een bol
def bol_vol(straal):
    return (4/3) * math.pi * (straal ** 3)

kubus_volume = kubus_vol(5)
bol_volume = bol_vol(4)

print(f"De inhoud van deze kubus is: {kubus_volume}")
print(f"De inhoud van deze bol is: {bol_volume}")