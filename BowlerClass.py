from BatterClass import Batter


class Bowler(Batter):
    """Represents a cricket bowler with additional attributes and methods for bowling statistics."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Bowler object with attributes from both Batter and bowling-specific attributes."""
        super().__init__(first_name, last_name, age)
        # Bowling-specific attributes
        self.wickets = 0
        self.runs_given = 0
        self.is_bowling = False  # Indicates if the bowler is currently bowling
        self.no_of_balls_bowled = 0  # Number of balls bowled

    # Getters (accessors) for bowling-specific attributes
    def get_is_bowling(self):
        """Returns True if the bowler is currently bowling, False otherwise."""
        return self.is_bowling

    def get_no_of_balls_bowled(self):
        """Returns the number of balls bowled by the bowler."""
        return self.no_of_balls_bowled

    def get_economy(self):
        """Calculates and returns the bowler's economy rate (runs conceded per over)."""
        if self.get_no_of_balls_bowled() > 0:
            # Calculate economy rate (runs per over => runs / (num of ball bowled / 6))
            return round(((self.runs_given * 6) / self.get_no_of_balls_bowled()), 2)
        else:
            # Return 0 if no balls have been bowled
            return 0

    def get_runs_given(self):
        """Returns the number of runs conceded by the bowler."""
        return self.runs_given

    def get_wickets(self):
        """Returns the number of wickets taken by the bowler."""
        return self.wickets

    def get_full_name(self):
        return super().get_full_name()

    # Methods to display bowler information
    def show_details(self):
        """Prints the bowler's details, including both batting and bowling statistics."""
        super().show_details()  # Print basic player details from Batter class
        print("Bowling:")
        if self.get_runs() or self.get_no_of_balls_bowled() > 0:
            # Print bowling statistics if the bowler has bowled
            print(f"Economy: {self.get_economy()} \n{self.get_wickets()}/{self.get_runs_given()}")
        else:
            print("Did not bowl yet.")

    # Increment functions for bowling statistics
    def increment_wickets(self):
        """Increments the bowler's wickets by 1."""
        self.wickets += 1

    def increment_runs_given(self, runs_conceded=1):
        """Increments the bowler's runs given by the specified amount."""
        self.runs_given += runs_conceded

    def increment_balls_bowled(self):
        """Increments the number of balls bowled by the bowler."""
        self.no_of_balls_bowled += 1
