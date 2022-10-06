class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served = 0

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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=['vanila','strawberry','chocolate']

    def icecream(self):
        for icecm in self.flavors:
            print(icecm.title())

icecream=IceCreamStand('Macdonald','Sundae Cone')
icecream.icecream()
#icecream.describe_restaurant()
#icecream.set_number_served(500)