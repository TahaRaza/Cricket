class Player:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_age(self):
        return self.age

    def show_details(self):
        print(f"Name: {self.get_full_name()}\n"
              f"Age: {self.get_age()}")
