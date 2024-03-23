import random
from datetime import date


def scoring_menu():
    # ------------------------Showing Score Menu----------------------------#
    print("\n\n")
    print("--------------------------------\n"
          "Press O for Out\n"
          "Press B for Boundary\n"
          "Press N for No Ball\n"
          "Press D for Dot Ball\n"
          "Press W for Wide Ball\n"
          "Press R for Runs Taken Between the Wicket\n"
          "Press L for Leg Bye and Bye \n"
          "Press E to End match due to Rain\n")
    return str.upper(input('What happened on this Ball: '))


class Match:
    _ball_counted = True

    @classmethod
    def set_ball_counted(cls, value):
        cls._ball_counted = value

    @classmethod
    def get_ball_counted(cls):
        return cls._ball_counted

    def __init__(self, team1, team2, match_type, stadium):
        self.team1 = team1
        self.team2 = team2
        self.stadium = stadium
        self.date = date.today().strftime("%Y-%m-%d")
        self.toss_winner = None
        self.toss_winner_decision = None
        self.current_innings = 1
        self.current_bowler = None
        self.batting_team = None
        self.bowling_team = None
        self.target = 0
        self.match_type = match_type
        self.total_overs = 0

    def simulate_match(self):
        self.set_total_overs()
        self.toss()  # simulates the toss and sets toss_winner and toss_winner_decision
        self.start_innings()
        self.innings()

    def toss(self):

        # ----------------------Toss--------------------#
        self.toss_winner = random.choice([self.team1, self.team2])
        print(f"{self.toss_winner.name} has won the toss!")

        while True:
            self.toss_winner_decision = input(f"{self.toss_winner.name} choose? (bat/bowl): ").lower()
            if self.toss_winner_decision in ["bat", "bowl"]:
                break
            print("Invalid choice. Please enter 'bat' or 'bowl'.")

        print(f"{self.toss_winner.name} has chosen to {self.toss_winner_decision} first.")

    def start_innings(self):
        print("Starting first innings")
        # ----------------------Starting First Innings--------------------#

        if self.toss_winner_decision == "bat":
            self.batting_team = self.toss_winner
            self.bowling_team = self.team2 if self.toss_winner == self.team1 else self.team1
        else:
            self.batting_team = self.team2 if self.toss_winner == self.team1 else self.team1
            self.bowling_team = self.toss_winner

        self.current_bowler = self.bowling_team.bowlers[self.bowling_team.get_int_over()]

        print(f"{self.batting_team.name} is batting. {self.bowling_team.name} is bowling.")

    def innings(self):

        # Handle switching innings or ending the match

        self.scoring(self.current_innings)
        if self.current_innings == 2:
            print('')
            self.second_innings()  # Proceed to second innings
        elif self.current_innings == 3:
            print('')
            self.show_complete_score()
            return

    def handle_out(self):
        # -------------------------Checking Out Type ------------------------------#
        while True:
            out_type = input("Enter the type of out (e.g., bowled, caught, LBW, run out, stump): ")
            valid_types = ["bowled", "caught", "lbw", "run out", "stump"]
            if out_type.lower() in valid_types:
                break
            else:
                print("Invalid out type. Please enter a valid type.")
        if out_type == "run out":
            self.handle_run_out()
            return

        self.batting_team.current_batters[0].dismissal_type = out_type
        self.batting_team.current_batters[0].is_out = True
        self.batting_team.current_batters[0].increment_balls_played()
        self.bowling_team.increment_wickets()
        self.bowling_team.current_bowler.increment_wickets()

        # -------------------------- Checking Caught and Printing-------------------------- #
        if out_type.lower() == 'caught':
            self.bowling_team.increment_ball()
            i = 1
            for player in self.bowling_team.batters:
                print(f" {i}: {player.get_full_name()}")
                i += 1
            while True:
                caught_by = int(input("The Player number from above who caught the catch(1-11): "))

                if 0 < caught_by < 12:
                    break
                else:
                    print("Invalid Number. Please enter a valid number (1 to 11).")

            if (self.bowling_team.batters[caught_by - 1].get_full_name() ==
                    self.bowling_team.current_bowler.get_full_name()):
                print(
                    f"\n\n{self.batting_team.current_batters[0].get_full_name()} is caught n Bowled "
                    f"by {self.bowling_team.batters[caught_by - 1].get_full_name()}.")
            else:
                print(
                    f"\n\n{self.batting_team.current_batters[0].get_full_name()} is Out!! Caught "
                    f"by {self.bowling_team.batters[caught_by - 1].get_full_name()}")
        elif out_type.lower() == "stump":
            is_wide = input("Was it a Wide Ball(y/n): ")
            if is_wide == "y":
                self.batting_team.increment_team_score(1)
                self.bowling_team.current_bowler.increment_runs_given(runs_conceded=1)
                self.bowling_team.increment_total_extras(total_extras=1)
            else:
                self.bowling_team.current_bowler.increment_balls_bowled()
                self.bowling_team.increment_ball()
            print(
                f"\n\n{self.batting_team.current_batters[0].get_full_name()} "
                f"is {self.batting_team.current_batters[0].dismissal_type} "
                f"by {self.bowling_team.current_bowler.get_full_name()}")
        else:
            self.bowling_team.increment_ball()
            print(
                f"\n\n{self.batting_team.current_batters[0].get_full_name()} "
                f"is {self.batting_team.current_batters[0].dismissal_type} "
                f"by {self.bowling_team.current_bowler.get_full_name()}")

        # -----------------Removing Out Player------------------------#

        self.batting_team.current_batters.remove(self.batting_team.current_batters[0])
        if self.bowling_team.get_total_wickets() < 10:
            self.batting_team.current_batters.append(self.batting_team.batters[self.bowling_team.get_total_wickets()+1])
        # -----------------Checking if Innings ended------------------------#
        self.is_innings_ended()

    def handle_boundary(self):
        while True:
            try:
                runs = int(input("Was it a six or four (Enter 6 or 4): "))
                if runs == 6 or runs == 4:
                    break  # Valid input received, exit the loop
                else:
                    print("Invalid input. Please enter 6 or 4.")
            except ValueError:
                print("Invalid input. Please enter a valid integer (6 or 4).")

        # Update batter's stats
        if runs == 4:
            self.batting_team.current_batters[0].increment_fours()
        elif runs == 6:
            self.batting_team.current_batters[0].increment_sixes()

        self.batting_team.current_batters[0].increment_balls_played()

        # # Update bowler's stats
        self.bowling_team.current_bowler.increment_balls_bowled()
        self.bowling_team.current_bowler.increment_runs_given(runs)

        # # Update team's total score
        self.bowling_team.increment_ball()
        self.batting_team.increment_runs(runs)  # will increase team runs and current batter runs

        print(f"{runs} runs scored!")

    def handle_no_ball(self):
        runs = int(input("How many runs were made on this Ball: "))
        self.batting_team.current_batters[0].balls_played += 1
        # Update batter's stats (runs scored, balls faced)
        if runs == 4:
            self.batting_team.current_batters[0].increment_fours()
            self.batting_team.increment_runs(5)
        elif runs == 6:
            self.batting_team.current_batters[0].increment_sixes()
            self.batting_team.increment_runs(7)
        else:
            self.batting_team.current_batters[0].increment_runs(runs)
            self.batting_team.increment_runs(runs + 1)
        # Update bowler's stats (runs conceded, no balls bowled)
        self.bowling_team.current_bowler.increment_runs_given(runs + 1)
        # Update team's total score and extras
        self.bowling_team.increment_total_extras(runs + 1)
        # Swap batters if needed
        if runs % 2 == 1:
            self.batting_team.current_batters.reverse()

        print("It's a Free Hit")  # Indicate free hit for the next ball
        self.set_ball_counted(False)

    def handle_dot_ball(self):
        self.bowling_team.increment_ball()
        self.bowling_team.get_current_bowler().increment_balls_bowled()
        self.batting_team.current_batters[0].balls_played += 1
        print("It's a Dot Ball")

    def handle_wide_ball(self):
        runs = int(input("How many Extra Runs team took on Wide: "))
        self.batting_team.increment_team_score(runs + 1)
        self.bowling_team.current_bowler.increment_runs_given(runs + 1)
        self.bowling_team.increment_total_extras(runs + 1)
        self.set_ball_counted(False)
        if runs % 2 == 1:
            self.batting_team.current_batters.reverse()

    def handle_runs(self, runs):
        self.batting_team.current_batters[0].increment_balls_played()
        # Update batter's stats (runs scored, balls faced)
        # Update bowler's stats (runs conceded)
        self.bowling_team.current_bowler.increment_runs_given(runs)
        self.bowling_team.current_bowler.increment_balls_bowled()
        # Update team's total score Update batter's stats (runs scored, balls faced)
        self.batting_team.increment_runs(runs)  # will increase team runs and current batter runs
        self.bowling_team.increment_ball()
        # Swap batters if needed
        if runs % 2 == 1:
            self.batting_team.current_batters.reverse()
        return runs

    def handle_exit(self):
        return

    def handle_leg_bye(self):
        bye_or_leg_bye = input("Was it bye or leg bye? (b/lb): ").lower()
        runs = int(input(f"How many runs were made on {bye_or_leg_bye}: "))
        self.batting_team.current_batters[0].runs -= runs
        self.handle_runs(runs=runs)

    def second_innings(self):
        self.set_target()
        print(f"Target:{self.target}")
        self.show_complete_score()

        print("\n_______________________________Starting Second Innings_______________________________\n")
        self.batting_team, self.bowling_team = self.bowling_team, self.batting_team
        print(f"batting team:{self.batting_team.name}")
        print(f"Bowling team:{self.bowling_team.name}")

        self.innings()

    def is_innings_ended(self):

        if self.current_innings == 2:
            if (self.batting_team.total_team_score == (self.target - 1) and
                    self.bowling_team.get_int_over() == self.total_overs):
                print("Match Has Ended in a Draw!")
                self.current_innings = 3
                return True
            elif self.batting_team.total_team_score >= self.target:
                print(f"\n\n--------------------Match is over--------------------\n\n"
                      f"{self.batting_team.name} won by {10 - self.bowling_team.total_team_wickets()} wickets!")
                self.current_innings = 3
                return True
            elif self.bowling_team.get_int_over() == self.total_overs:
                print(f"\n\n--------------------Match is over--------------------\n\n"
                      f" {self.bowling_team.name} won by "
                      f"{self.target - self.batting_team.total_team_score()} runs!")
                self.current_innings = 3
                return True

        if self.batting_team.total_team_wickets == 10:
            print("All out!")
            self.current_innings = 2
            self.total_overs = 0

        elif self.bowling_team.get_int_over() >= self.total_overs:
            print("Overs completed!")
            self.current_innings = 2

        return False

    def display_scorecard(self):
        print("\n_____________________________Scorecard_____________________________")
        print(f" Team 1: {self.team1.name}")
        print(f" Team 2: {self.team2.name}")
        print(f" Stadium: {self.stadium}")
        print(f" Date: {self.date}")
        print(f" Toss winner: {self.toss_winner.name}")
        print(f" Current Inning: {self.current_innings}")
        print(f" Batting Team: {self.batting_team.name}")
        print(f" Bowling Team: {self.bowling_team.name}")
        print(f" Total Score: {self.batting_team.total_team_score}")
        print(f" Total Wickets: {self.bowling_team.total_team_wickets}")
        print(f" Current Ball: {self.bowling_team.current_ball}")
        print(f" Current Over: {self.bowling_team.current_over}")
        print(f" Current Baller: {self.bowling_team.get_current_bowler().get_full_name()}\n"
              f" Economy: {self.bowling_team.get_current_bowler().get_economy()}")
        print(
            f" Batter on Strike: {self.batting_team.current_batters[0].get_full_name()}\n"
            f" Strike Rate: {self.batting_team.current_batters[0].get_strike_rate()}\n"
            f" Balls played by Batter: {self.batting_team.current_batters[0].balls_played}\n"
            f" Score made by Batter: {self.batting_team.current_batters[0].runs}\n")
        print(
            f" Batters on Pitch: {self.batting_team.current_batters[0].get_full_name()} "
            f"and {self.batting_team.current_batters[1].get_full_name()}\n\n")

    def check_set_batter(self):
        if self.bowling_team.current_ball % 6 == 0:
            self.batting_team.current_batters.reverse()

    def set_bowler(self):
        self.bowling_team.set_current_bowler()

    def set_target(self):
        self.target = self.batting_team.total_team_score + 1

    def set_total_overs(self):
        match self.match_type:
            case "Super Over: 1 Over Match":  # 1 overs
                self.total_overs = 1
            case "Fives: 5 Overs Match":  # 5 overs
                self.total_overs = 5
            case "T10: 10 Overs Match":  # 10 overs
                self.total_overs = 10
            case "T20: 20 Overs Match":  # 20 overs
                self.total_overs = 20
            case "ODI: 50 Overs Match":  # 50 overs
                self.total_overs = 50
            case _:
                raise ValueError("Invalid match type")

    def get_target(self):
        return self.target

    def handle_run_out(self):
        i = 1
        for player in self.bowling_team.batters:
            print(f" {i}: {player.get_full_name()}")
            i += 1

        run_out_by = int(input("The Player number from above who threw for Run out (1-11): "))

        is_striker = input("Was Striker run out or Non-striker (s/n): ")

        if is_striker == 's':
            is_striker = True
        elif is_striker == 'n':
            is_striker = False
        else:
            pass
            # Throw error

        runs = self.handle_runs(runs=int(input("How many runs were made on this Ball: ")))

        self.bowling_team.increment_wickets()
        self.bowling_team.increment_run_outs()
        if is_striker and runs % 2 == 0 or not is_striker and runs % 2 == 1:
            self.even_runs_run_out(run_out_by=run_out_by)
        elif is_striker and runs % 2 == 1 or not is_striker and runs % 2 == 0:
            self.odd_runs_run_out(run_out_by=run_out_by)

    def even_runs_run_out(self, run_out_by):
        self.batting_team.current_batters[0].dismissal_type = "run out"
        self.batting_team.current_batters[0].is_out = True
        # -----------------Removing Out Player------------------------#
        self.batting_team.current_batters.remove(self.batting_team.current_batters[0])
        #
        # self.is_innings1_ended()
        print(
            f"\n\n{self.batting_team.current_batters[0].get_full_name()} is Run Out "
            f"by {self.bowling_team.batters[run_out_by - 1].get_full_name()}")

    def odd_runs_run_out(self, run_out_by):
        self.batting_team.current_batters[1].dismissal_type = "run out"
        self.batting_team.current_batters[1].is_out = True
        # -----------------Removing Out Player------------------------#

        self.batting_team.current_batters.remove(self.batting_team.current_batters[1])
        # -----------------Checking if Innings ended------------------------#
        if self.bowling_team.get_total_wickets() < 10:
            self.batting_team.current_batters.append(
                self.batting_team.batters[self.bowling_team.get_total_wickets() + 1])
        else:
            print("All Out!!")

        print(
            f"\n\n{self.batting_team.current_batters[1].get_full_name()} is Run Out "
            f"by {self.bowling_team.batters[run_out_by - 1].get_full_name()}")

    def scoring(self, innings):

        while self.current_innings < innings + 1:
            input_ = scoring_menu()

            if input_ == "O":
                self.handle_out()
            elif input_ == "B":
                self.handle_boundary()
            elif input_ == "N":
                self.handle_no_ball()
            elif input_ == "D":
                self.handle_dot_ball()
            elif input_ == "W":
                self.handle_wide_ball()
            elif input_ == "R":
                self.handle_runs(int(input("How many runs were made on this Ball: ")))
            elif input_ == "L":
                self.handle_leg_bye()
            elif input_ == "E":
                self.handle_exit()

            if self.get_ball_counted():
                self.set_bowler()
                self.check_set_batter()
            else:
                self.set_ball_counted(True)

            self.display_scorecard()

            # Check if inning has end
            is_ended = self.is_innings_ended()
            if is_ended:
                return

    def show_complete_score(self):
        print(f"batting team:{self.batting_team.name}: ")
        for batter in self.batting_team.batters:
            print(f"{batter.get_full_name()}: {batter.runs}-{batter.balls_played} S/R: {batter.get_strike_rate()}")
        print(f"Bowling team:{self.bowling_team.name}: ")
        for bowler in self.bowling_team.bowlers:
            print(f"{bowler.get_full_name()}: {bowler.runs_given}-{bowler.no_of_balls_bowled} "
                  f"eco: {bowler.get_economy()}")
