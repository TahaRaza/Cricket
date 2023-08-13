from PlayerClass import Player


class Batter(Player):
    def __init__(self, first_name, last_name, age, runs, balls_played, is_on_strike, is_batting):
        super().__init__(first_name, last_name, age)
        self.runs = runs
        self.is_on_strike = is_on_strike
        self.is_batting = is_batting
        self.balls_played = balls_played

    def get_is_on_strike(self):
        return self.is_on_strike

    def get_is_batting(self):
        return self.is_batting

    def get_runs(self):
        return self.runs

    def get_balls_played(self):
        return self.balls_played

    def show_details(self):
        super().show_details()
        print("Batting:")
        if self.get_runs() or self.get_balls_played() > 0:
            print(f"{self.get_runs()} runs on {self.get_balls_played()} balls\n")
        else:
            print("Did not bat yet.")
