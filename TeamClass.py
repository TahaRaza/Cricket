from BowlerClass import Bowler
from BatterClass import Batter
from openpyxl import load_workbook


class Team:
    """Represents a cricket team with its players (batters and bowlers)."""

    def __init__(self, name):
        """Initializes a Team object with its name and empty player lists."""
        self.name = name
        self.batters = []  # Initialize array for batters
        self.bowlers = []  # Initialize array for bowlers
        self.current_ball = 0
        self.current_over = 0.0
        self.current_batters = None
        self.current_bowler = None
        self.total_team_score = 0  # Total team score
        self.total_team_wickets = 0  # Total team Wickets
        self.total_extras = 0  # Total extras

        # Add players during initialization
        self.add_players(self.name)

    def add_players(self, name):
        """Loads player data from an Excel spreadsheet and creates Batter and Bowler objects."""
        print("Adding players")
        try:
            # Load the workbook
            wb = load_workbook('Teams.xlsx')  # Open the Teams.xlsx file

            # Access the sheet by its name
            ws = wb[name]  # Select the sheet with the specified name

            # Add batters
            for r in range(2, 13):  # Iterate through rows 2 to 12 for batters
                data = [str(ws.cell(row=r, column=i).value) for i in range(1, 4)]  # Extract data from cells
                first_name, last_name, age = data  # Unpack player data
                batter = Batter(  # Create a Batter object
                    first_name,
                    last_name,
                    int(age)
                )
                self.batters.append(batter)  # Add the batter to the team

            self.current_batters = [self.batters[0], self.batters[1]]  # Current 2 batters on pitch

            # Add bowlers (using the same sheet, indices 8 to 12)
            for r in range(8, 13):  # Iterate through rows 8 to 12 for bowlers
                data = [str(ws.cell(row=r, column=i).value) for i in range(1, 4)]  # Extract data from cells
                first_name, last_name, age = data  # Unpack player data
                bowler = Bowler(  # Create a Bowler object
                    first_name,
                    last_name,
                    int(age)
                )
                self.bowlers.append(bowler)  # Add the bowler to the team

            self.current_bowler = self.bowlers[0]  # Current bowler

        except FileNotFoundError:
            print("Error: Teams.xlsx file not found.")
        except KeyError:
            print(f"Error: Sheet '{name}' not found in the workbook.")

    # Setter Functions --------------------------------
    def set_over(self):
        self.current_over = round(float(int(self.current_ball / 6) + (int(self.current_ball % 6)) * 0.1), 1)

    def set_current_bowler(self):
        if self.get_int_over() < 5:
            self.current_bowler = self.bowlers[self.get_int_over()]

    # Increment Functions --------------------------------
    def increment_total_extras(self, total_extras):
        self.total_extras += total_extras

    def increment_wickets(self):
        self.total_team_wickets += 1

    def increment_runs(self, runs_scored):
        """Increments the team's total runs, the current batter's runs, and updates relevant statistics."""
        self.total_team_score += runs_scored
        self.current_batters[0].increment_runs(runs_scored)

        # Update bowler's runs given and balls bowled
        self.current_bowler.increment_runs_given(runs_scored)
        self.current_bowler.increment_balls_bowled()

        # Increment ball and over count
        self.increment_ball()

    def increment_ball(self):
        self.current_ball += 1
        self.set_over()

    # Getter Functions --------------------------------

    def get_total_team_score(self):
        return self.total_team_score

    def get_total_wickets(self):
        return self.total_team_wickets

    def get_int_over(self):
        return int(self.current_over)

    def get_current_bowler(self):
        self.set_current_bowler()
        return self.current_bowler
