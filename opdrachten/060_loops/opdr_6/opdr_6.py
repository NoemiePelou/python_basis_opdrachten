# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

my_list = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']
my_list.insert(0, 'pepperoni')
my_list.remove('quattro stagioni')
my_list.sort()
print(my_list[:3])

#middelste pizza in de list
middle_pizza = my_list[len(my_list) // 2]
print(middle_pizza)

#laatste 3 pizzas in de list
last_three_pizzas = my_list[-3:]
print(last_three_pizzas)