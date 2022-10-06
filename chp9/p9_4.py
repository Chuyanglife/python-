class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f"This {self.restaurant_name} has {self.cuisine_type}.")
    def open_restaurant(self):
        print(f"{self.restaurant_name}, now is open.")
    def parasite_num(self):
        print(f"There are {self.number_served} people eating here.")
    def set_number_served(self,num):
        self.number_served=num
        print(f"There are {self.number_served} people eating here.")
    def increment_number_served(self,num_add):
        self.number_served+=num_add

restaurant=Restaurant('PizzaHut','Pizza')

restaurant.parasite_num()
restaurant.set_number_served(20)
restaurant.parasite_num()
restaurant.increment_number_served(10)
restaurant.parasite_num()