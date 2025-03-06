# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = { 
    "rijn": ["nederland", "duitsland", "frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}

# Lijst van riviernamen
rivieren = list(rivier_info.keys())

# 1e rivier
rivier_1 = rivieren[0].capitalize()
land_2_rivier_1 = rivier_info[rivieren[0]][1].capitalize()
print(f"De rivier {rivier_1} stroomt onder andere door {land_2_rivier_1}")

# 2e rivier
rivier_2 = rivieren[1].capitalize()
land_1_rivier_2 = rivier_info[rivieren[1]][0].capitalize()
print(f"De rivier {rivier_2} stroomt onder andere door {land_1_rivier_2}")

# 3e rivier
rivier_3 = rivieren[2].capitalize()
land_3_rivier_3 = rivier_info[rivieren[2]][2].capitalize()
print(f"De rivier {rivier_3} stroomt onder andere door {land_3_rivier_3}")
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....