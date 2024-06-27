import functions as f
from MatchClass import Match


def main():
    """Loads teams from an Excel file, prompts for team selection,
       creates Team objects, simulates a match, and displays results."""

    team_A, team_B = f.choose_team()
    match_type = f.choose_match_type()
    stadium_name = f.choose_location()

    match = Match(team1=team_A, team2=team_B, match_type=match_type, stadium=stadium_name)
    # winner, scorecard = match.simulate_match()
    match.simulate_match()


if __name__ == "__main__":
    main()

# TO-DO
