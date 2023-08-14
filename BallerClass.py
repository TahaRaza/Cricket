from BatterClass import Batter


class Baller(Batter):
    def __init__(self, first_name, last_name, age, runs, balls_played, is_on_strike, is_batting,
                 wickets, runs_given, is_balling, no_of_balls):
        super().__init__(first_name, last_name, age, runs, balls_played, is_on_strike, is_batting)
        self.wickets = wickets
        self.runs_given = runs_given
        self.is_bowling = is_balling
        self.no_of_balls = no_of_balls

    def get_is_balling(self):
        return bool(self.is_bowling)

    def get_no_of_balls(self):
        return int(self.no_of_balls)

    def economy(self):
        if self.get_no_of_balls() > 0:
            return float(round((self.runs_given * 6) / self.get_no_of_balls(), 2))
        else:
            return 0

    def get_runs_given(self):
        return int(self.runs_given)

    def get_wickets(self):
        return int(self.wickets)

    def show_details(self):
        super().show_details()
        print("Balling:")
        if self.get_runs() or self.get_no_of_balls() > 0:
            print(f"Economy: {float(self.economy())}\n{int(self.get_wickets())}/{int(self.get_runs_given())}")
        else:
            print("Did not ball yet.")