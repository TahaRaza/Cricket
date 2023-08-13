from openpyxl import load_workbook
from BallerClass import Baller
from BallerClass import Batter

# Load the workbook
global first_name, last_name, age, runs, balls_played, is_on_strike, is_batting, wickets, runs_given, \
    is_balling, no_of_balls
wb = load_workbook('Pakistan CT.xlsx')
# accessing first sheet by its name
ws = wb['Bat']


# Just made a team class for later
class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def get_players(self):
        return self.players
