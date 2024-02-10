import random
from datetime import date


class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.venue = input("Enter the venue of the match: ")
        self.date = date.today().strftime("%Y-%m-%d")
        self.toss_winner = None
        self.toss_winner_decision = None
        self.current_innings = 1
        self.batting_team = None
        self.bowling_team = None
        self.target = 0

    def simulate_match(self):
        self.toss()  # simulates the toss and sets toss_winner and toss_winner_decision
        self.start_innings()
        self.first_innings()

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

    def first_innings(self):
        self.scoring(self.current_innings)

        # Handle switching innings or ending the match
        if self.current_innings == 2:
            self.second_innings()  # Proceed to second innings
        elif self.current_innings == 3:
            return

    def scoring_menu(self):
        # ------------------------Showing Score Menu----------------------------#
        print("\n\n")
        print("--------------------------------\n"
              "Press O for Out\n"
              "Press B for Boundary\n"
              "Press N for No Ball\n"
              "Press D for Dot Ball\n"
              "Press W for Wide Ball\n"
              "Press R for Runs Taken Between the Wicket\n"
              "Press E to End match due to Rain\n")
        user_input = str.upper(input('What happened on this Ball: '))
        return user_input

    def handle_out(self):
        # -------------------------Checking Out Type ------------------------------#
        while True:
            out_type = input("Enter the type of out (e.g., bowled, caught, LBW): ")
            valid_types = ["bowled", "caught", "lbw"]
            if out_type.lower() in valid_types:
                break
            else:
                print("Invalid out type. Please enter a valid type.")

        self.batting_team.current_batters[0].dismissal_type = out_type  # additional
        self.batting_team.current_batters[0].is_out = True  # additional
        self.batting_team.current_batters[0].increment_balls_played()
        self.bowling_team.increment_wickets()
        self.bowling_team.increment_ball()
        self.bowling_team.bowlers[self.bowling_team.get_int_over()].increment_wickets()

        # -------------------------- Checking Caught and Printing-------------------------- #
        if out_type.lower() == 'caught':
            i = 1
            for player in self.bowling_team.batters:
                print(f" {i}: {player.get_full_name()}")
                i += 1
            while True:
                caught_by = int(input("The Player number from above who caught the catch(1-11): "))

                if caught_by < 12 and caught_by > 0:
                    break
                else:
                    print("Invalid NUmber. Please enter a valid number (1 to 11).")

            if self.bowling_team.batters[
                caught_by - 1].get_full_name() == self.bowling_team.current_bowler.get_full_name():
                print(
                    f"\n\n{self.batting_team.current_batters[0].get_full_name()} is caught n Bowled by {self.bowling_team.batters[caught_by - 1].get_full_name()}.")
            else:
                print(
                    f"\n\n{self.batting_team.current_batters[0].get_full_name()} is Out!! Caught by {self.bowling_team.batters[caught_by - 1].get_full_name()}")
        else:
            print(
                f"\n\n{self.batting_team.current_batters[0].get_full_name()} is {self.batting_team.current_batters[0].dismissal_type} by {self.bowling_team.current_bowler.get_full_name()}")

        # -----------------Removing Out Player------------------------#

        self.batting_team.current_batters.remove(self.batting_team.current_batters[0])

        # -----------------Checking if Innings ended------------------------#
        if self.bowling_team.get_total_wickets() < 10:
            self.batting_team.current_batters.append(
                self.batting_team.batters[self.bowling_team.get_total_wickets() + 1])
            self.batting_team.current_batters.reverse()
        else:
            print("All Out!!")

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
        self.batting_team.increment_runs(runs)

        print(f"{runs} runs scored!")

    def handle_no_ball(self):
        runs = int(input("How many runs were made on this Ball: "))
        self.batting_team.current_batters[0].balls_played += 1
        # Update batter's stats (runs scored, balls faced)
        if runs == 4:
            self.batting_team.current_batters[0].increment_fours()
            self.batting_team.increment_runs(1)
        elif runs == 6:
            self.batting_team.current_batters[0].increment_sixes()
            self.batting_team.increment_runs(1)
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

    def handle_dot_ball(self):
        self.bowling_team.increment_ball()
        self.bowling_team.get_current_bowler().increment_balls_bowled()
        self.batting_team.current_batters[0].balls_played += 1
        print("It's a Dot Ball")

    def handle_wide_ball(self):
        runs = int(input("How many Extra Runs team took on Wide: "))
        self.batting_team.increment_runs(runs + 1)
        self.bowling_team.current_bowler.increment_runs_given(runs + 1)
        self.bowling_team.increment_total_extras(runs + 1)

    def handle_runs(self):
        runs = int(input("How many runs were made on this Ball: "))
        self.batting_team.current_batters[0].balls_played += 1
        # Update batter's stats (runs scored, balls faced)
        self.batting_team.current_batters[0].increment_runs(runs)
        # Update bowler's stats (runs conceded)
        self.bowling_team.current_bowler.increment_runs_given(runs)
        self.bowling_team.current_bowler.increment_balls_bowled()
        # Update team's total score
        self.batting_team.increment_runs(runs)
        self.bowling_team.increment_ball()
        # Swap batters if needed
        if runs % 2 == 1:
            self.batting_team.current_batters.reverse()

    def second_innings(self):
        self.set_target()
        print(f"Targets:{self.target}")
        print(f"batting team:{self.batting_team.name}: ")
        for batters in self.batting_team.batters:
            print(f"{batters.get_full_name()}: {batters.runs}-{batters.balls_played} S/R: {batters.get_strike_rate()}")
        print(f"Bowling team:{self.bowling_team.name}: ")
        for bowlers in self.bowling_team.bowlers:
            print(f"{bowlers.get_full_name()}: {batters.runs_given}-{batters.no_of_balls} eco: {batters.get_economy()}")

        print("\n_______________________________Starting Second Innings_______________________________\n")
        self.batting_team, self.bowling_team = self.bowling_team, self.batting_team
        print(f"batting team:{self.batting_team.name}")
        print(f"Bowling team:{self.bowling_team.name}")

        self.first_innings()

    def is_innings_ended(self):

        if self.current_innings == 2:
            if self.batting_team.total_team_score == (self.target - 1) and self.bowling_team.get_int_over() == 5.0:
                print("Match Has Ended in a Draw!")
                self.current_innings += 1
                return True
            elif self.batting_team.total_team_score >= self.target:
                print(f"match is over\n {self.batting_team.name} won!")
                self.current_innings += 1
                return True
            elif self.bowling_team.get_int_over() == 5.0:
                print(f"match is over\n {self.bowling_team.name} won!")
                self.current_innings += 1
                return True

        if self.batting_team.total_team_wickets == 10:
            print("All out!")
            self.current_innings += 1
        elif self.bowling_team.get_int_over() == 5:
            print("Overs completed!")
            self.current_innings += 1

        return False

    def display_scorecard(self):
        print("\n_____________________________Scorecard_____________________________")
        print(f" Team 1: {self.team1.name}")
        print(f" Team 2: {self.team2.name}")
        print(f" Venue: {self.venue}")
        print(f" Date: {self.date}")
        print(f" Toss winner: {self.toss_winner.name}")
        print(f" Current Inning: {self.current_innings}")
        print(f" Batting Team: {self.batting_team.name}")
        print(f" Bowling Team: {self.bowling_team.name}")
        print(f" Total Score: {self.batting_team.total_team_score}")
        print(f" Total Wickets: {self.bowling_team.total_team_wickets}")
        print(f" Current Ball: {self.bowling_team.current_ball}")
        print(f" Current Over: {self.bowling_team.current_over}")
        print(
            f" Current Baller: {self.bowling_team.get_current_bowler().get_full_name()}\n Economy: {self.bowling_team.get_current_bowler().get_economy()}")
        print(
            f" Batter on Strike: {self.batting_team.current_batters[0].get_full_name()}\n Strike Rate: {self.batting_team.current_batters[0].get_strike_rate()}")
        print(
            f" Batters on Pitch: {self.batting_team.current_batters[0].get_full_name()} and {self.batting_team.current_batters[1].get_full_name()}")

    def check_set_batter(self):
        if self.bowling_team.current_ball % 6 == 0:
            self.batting_team.current_batters.reverse()

    def set_bowler(self):
        self.bowling_team.set_current_bowler()

    def set_target(self):
        self.target = self.batting_team.total_team_score + 1

    def get_target(self):
        return self.target

    def scoring(self, innings):
        while self.current_innings < innings + 1:
            input_ = self.scoring_menu()

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
                self.handle_runs()
            elif input_ == "E":
                break

            self.set_bowler()
            self.check_set_batter()
            self.display_scorecard()

            # Check if inning has end
            isEnded = self.is_innings_ended()
            if isEnded:
                return
