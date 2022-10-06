class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"This {self.restaurant_name} has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name}, now is open.")

restaurant = Restaurant('Pizza Hut','Pizza')
print(f"{restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()