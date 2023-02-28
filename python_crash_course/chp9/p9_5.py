class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attempts=0
    def describe_user(self):
        print(f"\nname: {self.first_name.title()} {self.last_name.title()}")
        print(f"age: {self.age}")
    def greet_user(self):
        print(f"Hello! {self.first_name.title()} {self.last_name.title()}")
   # def get_descriptive_name(self):
    #    full_name=f"{self.first_name} {self.last_name}"
     #   return full_name.title()
    def read_login_attempts(self):
        print(f"Login {self.login_attempts} times.")
    def increment_login_attempts(self,times):
        self.login_attempts+=times
        #return self.login_attempts
    def reset_login_attempts(self):
        self.login_attempts=0
        #return self.reset_login_attempts

user=User('ChuYang','Wong',23)
user.read_login_attempts()
#print(user.get_descriptive_name())
user.increment_login_attempts(50)
user.read_login_attempts()

user.increment_login_attempts(100)
user.read_login_attempts()

user.reset_login_attempts()
user.read_login_attempts()