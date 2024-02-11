class Player:
    """Represents a player with basic attributes, getters, setters, and display methods."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Player object with the given attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Getters (accessors) to retrieve the player's attributes
    def get_first_name(self):
        """Returns the player's first name."""
        return self.first_name

    def get_last_name(self):
        """Returns the player's last name."""
        return self.last_name

    def get_full_name(self):
        """Returns the player's full name (first name + last name)."""
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        """Returns the player's age."""
        return self.age

    # Setters (mutators) to modify the player's attributes
    def set_first_name(self, new_first_name):
        """Sets the player's first name."""
        self.first_name = new_first_name

    def set_last_name(self, new_last_name):
        """Sets the player's last name."""
        self.last_name = new_last_name

    def set_age(self, new_age):
        """Sets the player's age."""
        self.age = new_age

    # Methods to display player information
    def show_details(self):
        """Prints the player's basic details (name and age)."""
        print(f"Name: {self.get_full_name()}\nAge: {self.get_age()}")
