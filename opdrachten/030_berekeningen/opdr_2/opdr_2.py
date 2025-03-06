# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

c = ...
f = ...
def celsius_naar_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_naar_celsius(f):
    return (f - 32) * 5/9

# Eerste set van waarden
c = -12
f = 102

# Omrekeningen
f_omgerekend = celsius_naar_fahrenheit(c)
c_omgerekend = fahrenheit_naar_celsius(f)

# Output voor eerste set
print(f"{c} graden Celsius is gelijk aan {f_omgerekend:.1f} graden Fahrenheit")
print(f"{f} graden Fahrenheit is gelijk aan {c_omgerekend:.1f} graden Celsius")

# Tweede set van waarden
c = 62.2
f = 96

# Omrekeningen
f_omgerekend = celsius_naar_fahrenheit(c)
c_omgerekend = fahrenheit_naar_celsius(f)

# Output voor tweede set
print(f"{c} graden Celsius is gelijk aan {f_omgerekend:.1f} graden Fahrenheit")
print(f"{f} graden Fahrenheit is gelijk aan {c_omgerekend:.1f} graden Celsius")
