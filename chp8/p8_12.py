def make_pizza(*toppings):
    print(f"\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers')
make_pizza('mushrooms','extra cheese','green peppers')