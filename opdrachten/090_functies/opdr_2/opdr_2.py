# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(afile, atext):
    with open(afile, "a", encoding="utf-8") as file:
        file.write(atext + "\n")

#Zet kilometers om naar miles
def kilometers_naar_miles(km):
    return km / 1.609344

#Zet miles om naar kilometers
def miles_naar_kilometers(miles):
    return miles * 1.609344

kilometers = 1223
miles = 867

miles_converted = kilometers_naar_miles(kilometers)
km_converted = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_converted} miles")
print(f"{miles} miles = {km_converted} kilometers")

my_tekst = f"{kilometers} kilometers = {miles_converted} miles\n{miles} miles = {km_converted} kilometers"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
