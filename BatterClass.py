from PlayerClass import Player


class Batter(Player):
    """Represents a cricket batter with specific attributes and methods for batting statistics."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Batter object with attributes from Player and batting-specific attributes."""
        super().__init__(first_name, last_name, age)  # Inherit attributes from Player
        # Batting-specific attributes
        self.runs = 0  # Total runs scored
        self.is_on_strike = False  # Indicates if the batter is currently on strike
        self.is_batting = False  # Indicates if the batter is currently batting
        self.balls_played = 0  # Number of balls faced
        self.dismissal_type = None  # Type of dismissal (if out)
        self.is_out = False  # True if the batter is out, False otherwise
        self.fours = 0  # Number of fours hit
        self.sixes = 0  # Number of sixes hit
        self.strike_rate = 0

    # Getters (accessors) for batting-specific attributes
    def get_is_on_strike(self):
        """Returns True if the batter is currently on strike, False otherwise."""
        return self.is_on_strike

    def get_is_batting(self):
        """Returns True if the batter is currently batting, False otherwise."""
        return self.is_batting

    def get_runs(self):
        """Returns the total runs scored by the batter."""
        return self.runs

    def get_balls_played(self):
        """Returns the number of balls faced by the batter."""
        return self.balls_played

    def get_strike_rate(self):
        """Returns the Strike rate of the batter."""
        self.set_strike_rate()
        return self.strike_rate

    def get_full_name(self):
        return super().get_full_name()

    # Methods to display batter information
    def show_details(self):
        """Prints the batter's details, including both general and batting statistics."""
        super().show_details()  # Print basic player details from Player class
        print("Batting:")
        if self.get_runs() or self.get_balls_played() > 0:
            # Print batting statistics if the batter has batted
            print(f"{self.get_runs()} runs on {self.get_balls_played()} balls\n")
        else:
            print("Did not bat yet.")

    # Increment functions for batting statistics
    def increment_runs(self, runs_scored):
        """Increments the batter's runs by the specified amount."""
        self.runs += runs_scored

    def increment_balls_played(self):
        """Increments the number of balls faced by the batter."""
        self.balls_played += 1

    def increment_fours(self):
        """Increments the number of fours hit by the batter."""
        self.balls_played += 1
        self.fours += 1
        self.increment_runs(4)

    def increment_sixes(self):
        """Increments the number of sixes hit by the batter."""
        self.balls_played += 1
        self.sixes += 1
        self.increment_runs(6)

    # Setter for dismissal type
    def set_dismissal_type(self, dismissal_type):
        """Sets the type of dismissal for the batter."""
        self.dismissal_type = dismissal_type
        self.is_out = True  # Mark the better as out

    def set_strike_rate(self):
        if self.balls_played <= 0:
            self.strike_rate = 0
        else:
            self.strike_rate = round((self.runs * 100) / self.balls_played, 2)
