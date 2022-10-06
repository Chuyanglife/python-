class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print(f"\nname: {self.first_name.title()} {self.last_name.title()}")
        print(f"age: {self.age}")
    def greet_user(self):
        print(f"Hello! {self.first_name.title()} {self.last_name.title()}")

user1=User('ChuYang','Wong',23)
user2=User('Jackson','Wang',35)
user3=User('Bruce','Lee',54)

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()