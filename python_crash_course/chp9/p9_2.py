class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"This {self.restaurant_name} has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name}, now is open.")

restaurant1 = Restaurant('Pizza Hut','Pizza')
restaurant2 = Restaurant('Mcdonald','FilletOFish')
restaurant3 = Restaurant('KFC','Crispy Chicken')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()