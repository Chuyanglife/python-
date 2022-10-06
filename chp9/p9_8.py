class User:
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
    def get_descriptive_name(self):
        full_name=f"{self.first_name} {self.last_name}"
        return full_name.title()
    def read_login_attempts(self):
        print(f"Login {self.login_attempts} times.")
    def increment_login_attempts(self,times):
        self.login_attempts+=times
        #return self.login_attempts
    def reset_login_attempts(self):
        self.login_attempts=0
        #return self.reset_login_attempts

class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges=Privileges()

class Privileges:
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
        for permissions in self.privileges:
            print(permissions)

user=Admin('ChuYang','Wong',23)
user.privileges.show_privileges()