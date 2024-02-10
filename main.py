from TeamClass import Team
from MatchClass import Match

# teamName1 = input("Enter Team Name(e.g. Pakistan): ")
# teamName2 = input("Enter Team Name(e.g. India): ")
# team1 = Team(teamName2)
# team2 = Team(teamName1)


team1 = Team("Pakistan")
team2 = Team("India")

match = Match(team1, team2)
match.simulate_match()

# No ball 4/6 runs not added in score..
# Rahul  Chahar : SUS
# Player changed when over starts AND wide

#### Bowling team:Pakistan:  Second inning does not start rathar this error
# Traceback (most recent call last):
#   File "c:\Users\thraz\OneDrive\Desktop\CricketProject2\main.py", line 15, in <module>
#     match.simulate_match()
#   File "c:\Users\thraz\OneDrive\Desktop\CricketProject2\MatchClass.py", line 22, in simulate_match
#     self.first_innings()
#   File "c:\Users\thraz\OneDrive\Desktop\CricketProject2\MatchClass.py", line 59, in first_innings
#     self.second_innings()  # Proceed to second innings
#     ^^^^^^^^^^^^^^^^^^^^^
#   File "c:\Users\thraz\OneDrive\Desktop\CricketProject2\MatchClass.py", line 195, in second_innings
#     print(f"{bowlers.get_full_name()}: {batters.runs_given}-{batters.no_of_balls} eco: {batters.get_economy()}")
#                                         ^^^^^^^^^^^^^^^^^^
# AttributeError: 'Batter' object has no attribute 'runs_given'
# PS C:\Users\thraz\OneDrive\Desktop\CricketProject2>
