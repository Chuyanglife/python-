pizzas = ['beef','onion','tuna']
friend_pizzas = pizzas[:]
pizzas.append('pork')
friend_pizzas.append('chicken')
print(f"My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)
print(f"My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
